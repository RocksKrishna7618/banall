from telethon import TelegramClient
from config import API_ID, API_HASH, BOT_TOKEN, SUDO_USER

HANDLER = [] #jugar h vai jayda mat soch
SUDO_USERS = []
SUDO_USERS.append(SUDO_USER)


Zaid = TelegramClient('Cli1', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
