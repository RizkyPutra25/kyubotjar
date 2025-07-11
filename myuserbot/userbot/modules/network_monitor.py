
from telethon import events
from config import MIKROTIK_HOST, MIKROTIK_PORT, MIKROTIK_USER, MIKROTIK_PASS
import routeros_api

def connect_mikrotik():
    try:
        print("🔌 Coba konek ke MikroTik untuk monitoring...")
        connection = routeros_api.RouterOsApiPool(
            host=MIKROTIK_HOST,
            username=MIKROTIK_USER,
            password=MIKROTIK_PASS,
            port=MIKROTIK_PORT,
            plaintext_login=True
        )
        print("✅ Terhubung ke MikroTik (monitoring)")
        return connection.get_api()
    except Exception as e:
        print("❌ Gagal konek MikroTik (monitoring):", e)
        return None

@events.register(events.NewMessage(pattern=r"\.traffic (.+)"))
async def traffic_monitor_handler(event):
    interface = event.pattern_match.group(1)
    print(f"📥 Perintah .traffic {interface} diterima")

    api = connect_mikrotik()
    if not api:
        await event.reply("❌ Tidak dapat terhubung ke MikroTik.")
        return

    interface_data = api.get_resource("/interface").get(name=interface)
    if not interface_data:
        await event.reply(f"❌ Interface `{interface}` tidak ditemukan.")
        return

    stats = interface_data[0]
    msg = (
        f"📈 *Traffic Interface `{interface}`*
"
        f"↗️ TX: {int(stats['tx-byte']) / 1024:.2f} KB
"
        f"↘️ RX: {int(stats['rx-byte']) / 1024:.2f} KB"
    )
    await event.reply(msg)
