import os
from os import getenv

API_ID = int(os.environ.get("APP_ID", "6435225"))
API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
SUDO_USER = list(map(int, getenv("SUDO_USER").split()))
