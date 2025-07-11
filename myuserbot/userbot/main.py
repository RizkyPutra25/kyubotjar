from telethon import TelegramClient, events
from telethon.sessions import StringSession
from config import API_ID, API_HASH, STRING_SESSION
import userbot.modules.pppoe
import userbot.modules.network_monitor

client = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)

@client.on(events.NewMessage(pattern=r"\.ping"))
async def ping_handler(event):
    await event.reply("pong!")

print("🚀 Userbot sedang berjalan...")
client.start()
client.run_until_disconnected()
