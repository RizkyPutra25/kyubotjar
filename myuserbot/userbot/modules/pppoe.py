from telethon import events
from routeros_api import RouterOsApiPool
from config import MIKROTIK_HOST, MIKROTIK_USER, MIKROTIK_PASS, MIKROTIK_PORT

async def get_api():
    pool = RouterOsApiPool(
        host=MIKROTIK_HOST,
        username=MIKROTIK_USER,
        password=MIKROTIK_PASS,
        port=int(MIKROTIK_PORT),
        plaintext_login=True
    )
    return pool.get_api(), pool

@events.register(events.NewMessage(pattern=r"\.(pppoeactive|addpppoe|delpppoe)(?: |$)(.*)", incoming=True))
async def pppoe_handler(event):
    cmd = event.pattern_match.group(1)
    arg = event.pattern_match.group(2).strip()
    api, pool = await get_api()

    try:
        if cmd == "pppoeactive":
            active = api.get_resource('/ppp/active').get()
            msg = "**👥 PPPoE Active Users:**\n"
            msg += "\n".join([f"• {u['name']} — {u['address']}" for u in active]) or "Kosong."
            await event.reply(msg)

        elif cmd == "addpppoe":
            parts = arg.split()
            if len(parts) != 2:
                return await event.reply("Format: .addpppoe <username> <password>")
            name, passwd = parts
            api.get_resource('/ppp/secret').add(name=name, password=passwd, service='pppoe')
            await event.reply(f"✅ User PPPoE `{name}` berhasil dibuat.")

        elif cmd == "delpppoe":
            name = arg
            if not name:
                return await event.reply("Format: .delpppoe <username>")
            secrets = api.get_resource('/ppp/secret').get(name=name)
            if not secrets:
                return await event.reply(f"User `{name}` tidak ditemukan.")
            for s in secrets:
                api.get_resource('/ppp/secret').remove(id=s['.id'])
            await event.reply(f"🗑️ User PPPoE `{name}` berhasil dihapus.")
    except Exception as e:
        await event.reply(f"❗Error: {e}")
    finally:
        pool.disconnect()
