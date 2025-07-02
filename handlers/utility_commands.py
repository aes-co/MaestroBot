from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CommandHandler
from maestrobot.configs import CREATOR_CHANNEL_LINK, DONATION_LINK

async def id_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    user = update.effective_user
    if update.message.reply_to_message:
        target = update.message.reply_to_message.from_user
        text = f"🆔 <b>ID Pengguna:</b> <code>{target.id}</code>\n👤 <b>Nama:</b> {target.mention_html()}"
    else:
        text = (
            f"🆔 <b>ID Kamu:</b> <code>{user.id}</code>\n"
            f"👤 <b>Nama:</b> {user.mention_html()}\n"
            f"💬 <b>ID Chat:</b> <code>{chat.id}</code>"
        )
    await update.message.reply_text(text, parse_mode="HTML")

async def userinfo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.reply_to_message:
        user = update.message.reply_to_message.from_user
    else:
        if context.args:
            try:
                user = await context.bot.get_chat(context.args[0])
            except Exception:
                await update.message.reply_text("Gak nemu user itu, reply aja ke pesannya atau pakai username/id.")
                return
        else:
            user = update.effective_user
    text = (
        f"👤 <b>Nama:</b> {user.mention_html()}\n"
        f"🆔 <b>ID:</b> <code>{user.id}</code>\n"
        f"🔗 <b>Username:</b> @{user.username if user.username else '-'}\n"
        f"⏰ <b>Bot?</b> {'Ya' if user.is_bot else 'Bukan'}"
    )
    await update.message.reply_text(text, parse_mode="HTML")

async def groupinfo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    text = (
        f"👥 <b>Nama Grup:</b> {chat.title or '-'}\n"
        f"🆔 <b>ID Grup:</b> <code>{chat.id}</code>\n"
        f"👤 <b>Jumlah Member:</b> {await context.bot.get_chat_members_count(chat.id)}"
    )
    await update.message.reply_text(text, parse_mode="HTML")

async def linkchannel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if CREATOR_CHANNEL_LINK:
        await update.message.reply_text(
            f"👾 <b>Channel Wajib:</b>\nGabung dulu ke [Channel Ini]({CREATOR_CHANNEL_LINK}) biar bisa pakai semua fitur bot!",
            parse_mode="HTML",
            disable_web_page_preview=True
        )
    else:
        await update.message.reply_text("Belum ada channel creator yang diatur di bot ini.")

async def support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤝 <b>Butuh bantuan atau mau lapor bug?</b>\nGabung channel support kami ya!\n"
        "Telegram: @aesneverhere\n"
        "GitHub: https://github.com/aes-co/MaestroBot",
        parse_mode="HTML"
    )

async def donate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if DONATION_LINK:
        await update.message.reply_text(
            f"💖 <b>Dukung pengembangan MaestroBot!</b>\n"
            f"Kamu bisa traktir kopi atau donasi lewat link berikut:\n{DONATION_LINK}",
            parse_mode="HTML"
        )
    else:
        await update.message.reply_text("Belum ada link donasi yang diatur. Tapi makasih supportnya ya! 🙏")

def register(app):
    app.add_handler(CommandHandler("id", id_command))
    app.add_handler(CommandHandler("userinfo", userinfo))
    app.add_handler(CommandHandler("groupinfo", groupinfo))
    app.add_handler(CommandHandler("linkchannel", linkchannel))
    app.add_handler(CommandHandler("support", support))
    app.add_handler(CommandHandler("donate", donate))