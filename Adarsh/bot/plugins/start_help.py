#Adarsh goel
from Adarsh.bot import StreamBot
from Adarsh.vars import Var
import logging
logger = logging.getLogger(__name__)
from Adarsh.bot.plugins.stream import MY_PASS
from Adarsh.utils.human_readable import humanbytes
from Adarsh.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from Adarsh.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.name)
from pyrogram.types import ReplyKeyboardMarkup

                      
@StreamBot.on_message(filters.command('start') & filters.private)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{m.from_user.first_name}](tg://user?id={m.from_user.id}) Started !!"
        )
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        await m.reply_photo(
            photo="https://graph.org/file/7a20f5cb9c9e3a75285cb.jpg",
            caption="**ʜᴇʟʟᴏ...⚡\n\nɪᴀᴍ ᴀ sɪᴍᴘʟᴇ ᴛᴇʟᴇɢʀᴀᴍ ғɪʟᴇ/ᴠɪᴅᴇᴏ ᴛᴏ ᴘᴇʀᴍᴀɴᴇɴᴛ ʟɪɴᴋ ᴀɴᴅ sᴛʀᴇᴀᴍ ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ.**\n\n**ᴜsᴇ /help ғᴏʀ ᴍᴏʀᴇ ᴅᴇᴛᴀɪʟs\n\nsᴇɴᴅ ᴍᴇ ᴀɴʏ ᴠɪᴅᴇᴏ / ғɪʟᴇ ᴛᴏ sᴇᴇ ᴍʏ ᴘᴏᴡᴇʀ.\n\nᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴏᴜʀ ᴛᴇʟᴇɢᴛᴀᴍ ᴄʜᴀɴɴᴇʟ @DarkzArena ғᴏʀ ᴜᴘᴅᴀᴛᴇs.\nᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ᴛʜɪs ʙᴏᴛ ᴄʟɪᴄᴋ /about\n\nBy\n@NitinJack**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("⚡ UPDATES ⚡", url="https://t.me/darkzarena"), InlineKeyboardButton("⚡ SUPPORT ⚡", url="https://t.me/darkzarenabot")],
                    [InlineKeyboardButton("OWNER", url="https://t.me/nitinjack"), InlineKeyboardButton("📥 YT DOWNLOADER", url="https://t.me/ytdownloadrbot")],
                    [InlineKeyboardButton("💌 SUBSCRIBE 💌", url="https://www.youtube.com/channel/UCZbyDZOq6OrLPA3s97eizjA")]
                ]
            ),
            
        )
    else:

        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, ids=int(usr_cmd))

        file_size = None
        if get_msg.video:
            file_size = f"{humanbytes(get_msg.video.file_size)}"
        elif get_msg.document:
            file_size = f"{humanbytes(get_msg.document.file_size)}"
        elif get_msg.audio:
            file_size = f"{humanbytes(get_msg.audio.file_size)}"

        file_name = None
        if get_msg.video:
            file_name = f"{get_msg.video.file_name}"
        elif get_msg.document:
            file_name = f"{get_msg.document.file_name}"
        elif get_msg.audio:
            file_name = f"{get_msg.audio.file_name}"

        stream_link = "https://{}/{}".format(Var.FQDN, get_msg.id) if Var.ON_HEROKU or Var.NO_PORT else \
            "http://{}:{}/{}".format(Var.FQDN,
                                     Var.PORT,
                                     get_msg.id)

        msg_text = "**ᴛᴏᴜʀ ʟɪɴᴋ ɪs ɢᴇɴᴇʀᴀᴛᴇᴅ...⚡\n\n📧 ғɪʟᴇ ɴᴀᴍᴇ :-\n{}\n {}\n\n💌 ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ :- {}\n\n♻️ ᴛʜɪs ʟɪɴᴋ ɪs ᴘᴇʀᴍᴀɴᴇɴᴛ ᴀɴᴅ ᴡᴏɴ'ᴛ ɢᴇᴛ ᴇxᴘɪʀᴇᴅ ♻️\n\n<b>❖ YouTube.com/@mastertricknology</b>**"
        await m.reply_text(            
            text=msg_text.format(file_name, file_size, stream_link),
            
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⚡ ᴅᴏᴡɴʟᴏᴀᴅ ɴᴏᴡ ⚡", url=stream_link)]])
        )


@StreamBot.on_message(filters.command('help') & filters.private)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started !!"
        )
              
    await message.reply_photo(
            photo="https://graph.org/file/7a20f5cb9c9e3a75285cb.jpg",
            caption="**┣⪼ sᴇɴᴅ ᴍᴇ ᴀɴʏ ғɪʟᴇ/ᴠɪᴅᴇᴏ ᴛʜᴇɴ ɪ ᴡɪʟʟ ʏᴏᴜ ᴘᴇʀᴍᴀɴᴇɴᴛ sʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ ᴏғ ɪᴛ...\n\n┣⪼ ᴛʜɪs ʟɪɴᴋ ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴏʀ ᴛᴏ sᴛʀᴇᴀᴍ ᴜsɪɴɢ ᴇxᴛᴇʀɴᴀʟ ᴠɪᴅᴇᴏ ᴘʟᴀʏᴇʀs ᴛʜʀᴏᴜɢʜ ᴍʏ sᴇʀᴠᴇʀs.\n\n┣⪼ ғᴏʀ sᴛʀᴇᴀᴍɪɴɢ ᴊᴜsᴛ ᴄᴏᴘʏ ᴛʜᴇ ʟɪɴᴋ ᴀɴᴅ ᴘᴀsᴛᴇ ɪᴛ ɪɴ ʏᴏᴜʀ ᴠɪᴅᴇᴏ ᴘʟᴀʏᴇʀ ᴛᴏ sᴛᴀʀᴛ sᴛʀᴇᴀᴍɪɴɢ.\n\n┣⪼ ᴛʜɪs ʙᴏᴛ ɪs ᴀʟsᴏ sᴜᴘᴘᴏʀᴛ ɪɴ ᴄʜᴀɴɴᴇʟ. ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴀs ᴀᴅᴍɪɴ ᴛᴏ ɢᴇᴛ ʀᴇᴀʟᴛɪᴍᴇ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ ғᴏʀ ᴇᴠᴇʀʏ ғɪʟᴇs/ᴠɪᴅᴇᴏs ᴘᴏsʏ../\n\n┣⪼ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ :- /about\n\n\nᴘʟᴇᴀsᴇ sʜᴀʀᴇ ᴀɴᴅ sᴜʙsᴄʀɪʙᴇ**", 
  
        
        reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("⚡ UPDATES ⚡", url="https://t.me/darkzarena"), InlineKeyboardButton("⚡ SUPPORT ⚡", url="https://t.me/darkzarenabot")],
                    [InlineKeyboardButton("OWNER", url="https://t.me/nitinjack"), InlineKeyboardButton("📥 YT DOWNLOADER", url="https://t.me/ytdownloadrbot")],
                    [InlineKeyboardButton("💌 SUBSCRIBE 💌", url="https://www.youtube.com/channel/UCZbyDZOq6OrLPA3s97eizjA")]
                ]
            ),
            
        )

@StreamBot.on_message(filters.command('about') & filters.private)
async def about_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started !!"
        )
    await message.reply_photo(
            photo="https://graph.org/file/7a20f5cb9c9e3a75285cb.jpg",
            caption="""<b>sᴏᴍᴇ ʜɪᴅᴅᴇɴ ᴅᴇᴛᴀɪʟs😜</b>

<b>╭━━━━━━━〔ғɪʟᴇ ᴛᴏ ʟɪɴᴋ ʙᴏᴛ〕</b>
┃
┣⪼<b>ʙᴏᴛ ɴᴀᴍᴇ : ғɪʟᴇ ᴛᴏ ʟɪɴᴋ
┣⪼<b>ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/darkzarena'>Darkz Arena</a></b>
┣⪼<b>sᴜᴘᴘᴏʀᴛ : <a href='https://t.me/darkzarenabot'>Darkz Arena Support</a></b>
┣⪼<b>ᴏᴡɴᴇʀ   : @NitinJack</b>
┣⪼<b>sᴛᴏʀᴀɢᴇ : ᴜɴʟɪᴍɪᴛᴇᴅ</b>
┣⪼<b>ʟᴀɴɢᴜᴀɢᴇ: ᴘʏᴛʜᴏɴ 3</b>
┣⪼<b>ᴛʜᴀɴᴋs ᴛᴏ: ᴀᴅᴀʀsʜ, ᴊᴏᴇʟ</b>
┣⪼<b>ʏᴏᴜᴛᴜʙᴇ : <a href='https://youtube.com/@mastertricknology'>Master Tricknology</a></b>
┃
<b>╰━━━━━━━〔ᴘʟᴇᴀsʀ sᴜᴘᴘᴏʀᴛ ᴀɴᴅ ᴊᴏɪɴ ᴍʏ ᴄʜᴀɴɴᴇʟ〕</b>""",
  
        
        reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("⚡ UPDATES ⚡", url="https://t.me/darkzarena"), InlineKeyboardButton("⚡ SUPPORT ⚡", url="https://t.me/darkzarenabot")],
                    [InlineKeyboardButton("OWNER", url="https://t.me/nitinjack"), InlineKeyboardButton("📥 YT DOWNLOADER", url="https://t.me/ytdownloadrbot")],
                    [InlineKeyboardButton("💌 SUBSCRIBE 💌", url="https://www.youtube.com/channel/UCZbyDZOq6OrLPA3s97eizjA")]
                ]
            ),
            
        )
