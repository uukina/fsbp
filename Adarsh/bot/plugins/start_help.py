# (c) adarsh-goel 
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

if MY_PASS:
            buttonz=ReplyKeyboardMarkup(
            [
                ["START🌸","HELP🌼","LOGIN🔑","DC"],
                ["FOLLOW💙","PING❗","STATUS📊","DONASI🌷"]
                        
            ],
            resize_keyboard=True
        )
else:
            buttonz=ReplyKeyboardMarkup(
            [
                ["START🌸","HELP🌼","DC"],
                ["FOLLOW💙","PING❗","STATUS📊","DONASI🌷"]
                        
            ],
            resize_keyboard=True
        )

            
            
@StreamBot.on_message((filters.command("start") | filters.regex('START🌸')) & filters.private )
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"**Pengguna Baru** \n\n__User__ [{m.from_user.first_name}](tg://user?id={m.from_user.id}) __Terdaftar Sebagai Pengguna Bot !!__"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "kicked":
                await b.send_message(
                    chat_id=m.chat.id,
                    text="__Maaf Kamu Telah Di Banned. Silahkan Hubungi Owner__",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
             await StreamBot.send_photo(
                chat_id=m.chat.id,
                photo="https://i.pinimg.com/originals/c0/1d/02/c01d02a50d9f84de5ad8919241ebe42e.gif",
                caption="<i>JOIN CHANNEL UNTUK MENGGUNAKAN BOT🔐</i>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("JOIN CHANNEL✅", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
             return
        except Exception:
            await b.send_message(
                chat_id=m.chat.id,
                text="<i>Terjadi Kesalahan</i>",
                
                disable_web_page_preview=True)
            return
    await StreamBot.send_photo(
        chat_id=m.chat.id,
        photo ="https://i.pinimg.com/originals/59/55/a5/5955a5af7644598321720c1e682dc6eb.gif",
        caption =f'Hi {m.from_user.mention(style="md")}!,\n Saya adalah Bot Telegram yang diprogram untuk Mendapatkan Direct Link File Telegram.\nKirim / Foward File Apapun Untuk Mendapatkan Direct Link Download',
        reply_markup=buttonz)


@StreamBot.on_message((filters.command("help") | filters.regex('HELP🌼')) & filters.private )
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"**Pengguna Baru**\n\n__User__ [{message.from_user.first_name}](tg://user?id={message.from_user.id}) __Terdaftar Sebagai Pengguna Bot__"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="<i>Maaf Kamu Telah Di Banned. Silahkan Hubungi Owner</i>",
                    
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await StreamBot.send_photo(
                chat_id=message.chat.id,
                photo="https://i.pinimg.com/originals/c0/1d/02/c01d02a50d9f84de5ad8919241ebe42e.gif",
                Caption="**JOIN CHANNEL UNTUK MENGGUNAKAN BOT**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("JOIN CHANNEL✅", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="__Terjadi Kesalahan__",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text="""<b> Kirim / Foward File Apapun Untuk Mendapatkan Direct Link Download</b>""",
        
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("💁‍♂️ Owner", url="https://t.me/kardusbekasmie")]
            ]
        )
    )
