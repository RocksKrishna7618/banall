from Zaid import HANDLER, Zaid
from telethon import TelegramClient, events
from config import
import sys

@Zaid.on(events.NewMessage(pattern="^[?!/]clone"))
async def clone(msg):
    chat = msg.chat_id
    text = await msg.reply("Usage:\n\n /clone token")
    phone = msg.text.split(maxsplit=1)[1]
    try:
        await text.edit("Booting Your Client")
        client = TelegramClient(":memory:", api_id=API_ID, api_hash=API_HASH)
        await client.start(bot_token=phone)
        sys.modules["Zaid.plugins." + plugin_name] = load
        await text.edit("🔥 Booted Plugin⚡ " + plugin_name)
        user = await client.get_me()
        userid = telethon.utils.get_peer_id(user)
        await msg.reply(f"Your Client Has Been Successfully Started As {userid}! ✅\n\nThanks for Cloning.\nDon't Forget to Join Our @TheUpdatesChannel")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")
#End
