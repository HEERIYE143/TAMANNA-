from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import random
import requests
from SHUKLAMUSIC import app 

SUPPORT_CHAT = "KING_BHAI_BABY"

@app.on_message(filters.command("wish"))
async def wish(_, m):
    if len(m.command) < 2:
        await m.reply("𝐀ᴅᴅ 𝐖ɪꜱʜ 𝐁ᴀʙʏ🥀!")
        return 

    api = requests.get("https://nekos.best/api/v2/happy").json()
    url = api["results"][0]['url']
    text = m.text.split(None, 1)[1]
    wish_count = random.randint(1, 100)
    wish = f"❣️ 𝐇ᴇʏ... {m.from_user.first_name}! "
    wish += f"😉 𝐘ᴏᴜʀ 𝐖ɪꜱʜ ➻ {text} "
    wish += f"🤫 𝐏ᴏꜱꜱɪʙʟᴇ 𝐓ᴏ ➻ {wish_count}%"
    
    await app.send_animation(
        chat_id=m.chat.id,
        animation=url,
        caption=wish,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🥺 𝐒ᴜᴘᴘᴏʀᴛ 🥺", url=f"https://t.me/{SUPPORT_CHAT}")]])
    )
            
    
BUTTON = [[InlineKeyboardButton("🥺 𝐒ᴜᴘᴘᴏʀᴛ 🥺", url=f"https://t.me/{SUPPORT_CHAT}")]]
CUTIE = "https://telegra.ph/file/b948981351c0ffeaec2dd.jpg"

@app.on_message(filters.command("cute"))
async def cute(_, message):
    if not message.reply_to_message:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
    else:
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name

    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    CUTE = f"🍑 {mention} {mm}% 𝐂ᴜᴛᴇ 𝐁ᴀʙʏ🥀"

    await app.send_document(
        chat_id=message.chat.id,
        document=CUTIE,
        caption=CUTE,
        reply_markup=InlineKeyboardMarkup(BUTTON),
        reply_to_message_id=message.reply_to_message.message_id if message.reply_to_message else None,
    )
    
help_text = """
» ᴡʜᴀᴛ ɪꜱ ᴛʜɪꜱ (ᴡɪꜱʜ):
ʏᴏᴜ ʜᴀᴠɪɴɢ ᴀɴʏ ᴋɪɴᴅ ᴏꜰ 
(ᴡɪꜱʜᴇꜱ) ʏᴏᴜ ᴄᴀɴ ᴜꜱɪɴɢ ᴛʜɪꜱ ʙᴏᴛ ᴛᴏ ʜᴏᴡ ᴘᴏꜱꜱɪʙʟᴇ ᴛᴏ ʏᴏᴜʀ ᴡɪꜱʜ!
ᴇxᴀᴍᴘʟᴇ:» /wish : ɪ ᴡᴀɴᴛ ᴄʟᴀꜱꜱ ᴛᴏᴘᴘᴇʀ 
» /wish : ɪ ᴡᴀɴᴛ ᴀ ɴᴇᴡ ɪᴘʜᴏɴᴇ 
» /cute : ʜᴏᴡ ᴍᴜᴄʜ ɪ ᴀᴍ ᴄᴜᴛᴇ 
"""
