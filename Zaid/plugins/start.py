from Zaid import HANDLER
from telethon import events, Button

START_IMG = "https://telegra.ph/file/4cee76750b35007053c0d.jpg"
PM_START_TEXT = """
ʜᴇʏᴀ! {}
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘ **ɪ'ᴍ ᴀ ꜱɪᴍᴘʟᴇ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ**.
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘ **ᴄʟɪᴄᴋ ᴏɴ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ 🔘 ꜰᴏʀ ᴍᴏʀᴇ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ℹ️**.
"""

@events.register(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):
    if event.is_private:
       await event.client.send_file(event.chat_id,
             START_IMG,
             caption=PM_START_TEXT.format(event.sender.first_name), 
             buttons=[
        [Button.url("👨‍💻 ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", "https://github.com/ITZ-ZAID/Telethon-Music")],
        [Button.url("🗣️ ꜱᴜᴘᴘᴏʀᴛ", f"https://t.me/TheSupportChat"), Button.url("📣 ᴜᴘᴅᴀᴛᴇꜱ", f"t.me/TheUpdatesChannel")],
       return

    if event.is_group:
       await event.reply("**ʜᴇʏ! ɪ'ᴍ ꜱᴛɪʟʟ ᴀʟɪᴠᴇ ✅**")
       return


HANDLER.append(stac)
HANDLER.append(start)
