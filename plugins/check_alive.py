import time
import random
from pyrogram import Client, filters

CMD = ["/", "."]

@client.on_message(filters.command("alive", CMD))
async def check_alive(_, message):
    await message.reply_text("Lᴜᴄᴋʟʏ I Aᴍ Aʟɪᴠᴇ :) Pʀᴇss 👉 /start \n\nPʀᴇss 👉 /help Fᴏʀ Hᴇʟᴩ ;)\n\n\nPʀᴇss 👉 /ping Tᴏ Cʜᴇᴄᴋ Mʏ Pɪɴɢ 😁")

@client.on_message(filters.command("help", CMD))
async def help(_, message):
    await message.reply_text("Pʀᴇss 👉 /movies Tᴏ Kɴᴏᴡ Hᴏᴡ Tᴏ Rᴇǫᴜᴇsᴛ Mᴏᴠɪᴇs Iɴ A Pʀᴏᴩᴇʀ Wᴀʏ 📃\n\nPʀᴇss 👉 /series Tᴏ Kɴᴏᴡ Hᴏᴡ Tᴏ Rᴇǫᴜᴇsᴛ Sᴇʀɪᴇs Iɴ A Pʀᴏᴩᴇʀ Wᴀʏ 📃\n\n\nPʀᴇss 👉 /tutorial Fᴏʀ Tᴜᴛᴏʀɪᴀʟ Aʙᴏᴜᴛ Hᴏᴡ Tᴏ Gᴇᴛ Dɪʀᴇᴄᴛ Fɪʟᴇs Fʀᴏᴍ Mᴇ 🤗")

@client.on_message(filters.command("credits", CMD))
async def credits(_, message):
    await message.reply_text("ᴛʜɪs ɪs ᴄᴏᴅᴇᴅ ʙʏ KKMOVIES")

@client.on_message(filters.command("download", CMD))
async def tutorial(_, message):
    await message.reply_text("ғɪʀsᴛ ᴊᴏɪɴ ɪɴ ᴛʜᴇsᴇ ᴄʜᴀɴɴᴇʟs, ʏᴏᴜ ᴄᴀɴ ᴏɴʟʏ ᴀʙʟᴇ ᴛᴏ ᴜsᴇ ᴏᴜʀ ʙᴏᴛ ɪғ ʏᴏᴜʀᴇ ᴍᴇᴍʙᴇʀ ᴏғ ᴛʜɪs ᴄʜᴀɴɴᴇʟs. 👇👇 \n\n http://t.me/+u6G9wOGWt6Q4NTk1\n_______________________\n\nᴀғᴛᴇʀ ᴊᴏɪɴɪɴɢ ɪɴ ᴛʜᴇsᴇ ᴄʜᴀɴɴᴇʟs ᴛʏᴘᴇ ᴛʜᴇ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ/sᴇʀɪᴇs ᴀɴᴅ ʏᴏᴜʟʟ ɢᴇᴛ ᴛʜᴇ ғɪʟᴇs ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴀᴅs\n______________\n\nɴᴏᴛ
