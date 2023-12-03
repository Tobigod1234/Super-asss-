import os
import logging
import asyncio
from logging.handlers import RotatingFileHandler
from pyrogram import Client
from dotenv import load_dotenv

LOG_FILE_NAME = "Encoder@Log.txt"

if os.path.exists(LOG_FILE_NAME):
    with open(LOG_FILE_NAME, "r+") as f_d:
        f_d.truncate(0)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=2097152000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.INFO)
logging.getLogger("urllib3").setLevel(logging.INFO)
LOGS = logging.getLogger(__name__)


THUMB = "https://telegra.ph/file/1c2a8f45940e4cb43dbeb.jpg"
os.system(f"wget {THUMB} -O thumb.jpg")
ffmpeg = []
ffmpeg.append("-map 0 -c:v libx265 -crf 24 -c:s copy  -s 1280x720 -preset veryfast -c:a libopus -ab 60k -vbr 2 -ac 2 -level 2.1")
try:
    api_id = int(os.environ.get("API_ID", default="3847632"))
    api_hash = os.environ.get("API_HASH", default="1a9708f807ddd06b10337f2091c67657")
    bot_token = os.environ.get("BOT_TOKEN", default="6312969509:AAFZDMCTXtxKXenbk-Bp5kX4aGUAwFp9am8")
    DATABASE_URL = os.environ.get("DATABASE_URL", default="mongodb+srv://itzmeproman:itzmeproman@itzmeproman.qsmy0ka.mongodb.net/?retryWrites=true&w=majority")
    BOT_USERNAME = "neswtsbot"
    MAX_MESSAGE_LENGTH = 4096
    download_dir = os.environ.get("DOWNLOAD_DIR", "downloads/")
    sudo_users = list(set(int(x) for x in os.environ.get("SUDO_USERS").split()))
    sudo_users.append(6748415360)
    sudo_users.append(6748415360)
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", default=-1002108819224)
except Exception as e:
    LOGS.info("ENV Are Missing")

app = Client("nirusaki", api_id=api_id, api_hash=api_hash, bot_token=bot_token, workers=2)
0
data = []

if not download_dir.endswith("/"):
  download_dir = str(download_dir) + "/"
if not os.path.isdir(download_dir):
  os.makedirs(download_dir)
