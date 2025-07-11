
from telethon import events
from config import MIKROTIK_HOST, MIKROTIK_PORT, MIKROTIK_USER, MIKROTIK_PASS
import routeros_api

def connect_mikrotik():
    try:
        connection = routeros_api.RouterOsApiPool(
            host=MIKROTIK_HOST,
            username=MIKROTIK_USER,
            password=MIKROTIK_PASS,
            port=MIKROTIK_PORT,
            plaintext_login=True
        )
        return connection.get_api()
    except Exception as e:
        return None

@events.register(events.NewMessage(pattern=r"\.pppoeactive"))
async def pppoe_active_handler(event):
    api = connect_mikrotik()
    if not api:
        await event.reply("❌ Tidak dapat terhubung ke MikroTik.")
        return

    ppp_users = api.get_resource("/ppp/active").get()
    if not ppp_users:
        await event.reply("📡 Tidak ada user PPPoE yang aktif.")
        return

    msg = "📡 *User PPPoE Aktif:*
"
    for user in ppp_users:
        msg += f"• `{user['name']}` — `{user['address']}`\n"

    await event.reply(msg)
