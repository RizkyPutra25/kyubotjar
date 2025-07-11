from telethon import events
from routeros_api import RouterOsApiPool
from config import MIKROTIK_HOST, MIKROTIK_PORT, MIKROTIK_USER, MIKROTIK_PASS

async def get_api():
    pool = RouterOsApiPool(
        host=MIKROTIK_HOST,
        username=MIKROTIK_USER,
        password=MIKROTIK_PASS,
        port=int(MIKROTIK_PORT),
        plaintext_login=True
    )
    return pool.get_api(), pool

@events.register(events.NewMessage(pattern=r"\.(pppoeactive|dhcpactive|pppoeinterface|ifaceinfo|traffic)(?: |$)(.*)", incoming=True))
async def monitor_handler(event):
    cmd = event.pattern_match.group(1)
    arg = event.pattern_match.group(2).strip()
    api, pool = await get_api()

    try:
        if cmd == "pppoeactive":
            active = api.get_resource('/ppp/active').get()
            msg = "**👥 PPPoE Active Users:**\n"
            msg += "\n".join([f"• {u['name']} — {u['address']}" for u in active]) or "Kosong."
            await event.reply(msg)

        elif cmd == "dhcpactive":
            leases = api.get_resource("/ip/dhcp-server/lease").get()
            if not leases:
                await event.reply("🔍 Tidak ada client DHCP yang aktif.")
                return
            msg = "**📋 DHCP Clients:**\n"
            for lease in leases:
                msg += f"• {lease.get('host-name', '(unknown)')} - {lease['address']} ({lease['mac-address']})\n"
            await event.reply(msg)

        elif cmd == "pppoeinterface":
            interfaces = api.get_resource("/interface/pppoe-client").get()
            if not interfaces:
                return await event.reply("🚫 Tidak ada interface PPPoE ditemukan.")
            msg = "**📡 Interface PPPoE:**\n"
            for iface in interfaces:
                name = iface.get("name", "unknown")
                running = iface.get("running", "false")
                msg += f"• {name} — {'🟢 aktif' if running == 'true' else '🔴 tidak aktif'}\n"
            await event.reply(msg)

        elif cmd == "ifaceinfo":
            interfaces = api.get_resource("/interface").get()
            msg = "**🌐 Interface Status:**\n"
            for iface in interfaces:
                name = iface["name"]
                status = iface.get("running", "no")
                type_ = iface.get("type", "-")
                msg += f"• {name} ({type_}) - {'🟢 Aktif' if status == 'true' else '🔴 Mati'}\n"
            await event.reply(msg)

        elif cmd == "traffic":
            if not arg:
                return await event.reply("Gunakan: `.traffic <nama_interface>` (mis: ether1)")
            traffic = api.get_resource("/interface/monitor-traffic").call("monitor-traffic", {
                "interface": arg,
                "once": True
            })
            if not traffic:
                return await event.reply("Interface tidak ditemukan atau tidak aktif.")
            stat = traffic[0]
            rx = int(stat.get("rx-bits-per-second", 0)) // 1000
            tx = int(stat.get("tx-bits-per-second", 0)) // 1000
            await event.reply(f"📈 Trafik *{arg}*:\n⬇️ Download: {rx} kbps\n⬆️ Upload: {tx} kbps")
    except Exception as e:
        await event.reply(f"❗ Error: {e}")
    finally:
        pool.disconnect()
