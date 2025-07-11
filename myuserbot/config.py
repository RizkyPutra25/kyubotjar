from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Telegram API
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
STRING_SESSION = os.getenv("STRING_SESSION")

# MikroTik Config
MIKROTIK_HOST = os.getenv("MIKROTIK_HOST")
MIKROTIK_PORT = int(os.getenv("MIKROTIK_PORT"))
MIKROTIK_USER = os.getenv("MIKROTIK_USER")
MIKROTIK_PASS = os.getenv("MIKROTIK_PASS")
