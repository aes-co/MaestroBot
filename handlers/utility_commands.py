from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes, CommandHandler
from maestrobot.configs import CREATOR_CHANNEL_LINK, DONATION_LINK


async def id_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    chat = update.effective_chat
    if update.message.reply_to_message:
        target = update.message.reply_to_message.from_user
        text = (
            f"🆔 <b>ID Pengguna:</b> <code>{target.id}</code>\n"
            f"👤 <b>Nama:</b> {target.mention_html()}"
        )
    else:
        text = (
            f"🆔 <b>ID Kamu:</b> <code>{user.id}</code>\n"
            f"👤 <b>Nama:</b> {user.mention_html()}\n"
            f"💬 <b>ID Chat:</b> <code>{chat.id}</code>"
        )
    await update.message.reply_text(text, parse_mode="HTML")


async def userinfo_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.reply_to_message:
        user = update.message.reply_to_message.from_user
    elif context.args:
        try:
            user = await context.bot.get_chat(context.args[0])
        except Exception:
            await update.message.reply_text("User tidak ditemukan. Gunakan ID atau username yang valid.")
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


async def groupinfo_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    member_count = await context.bot.get_chat_member_count(chat.id)
    text = (
        f"👥 <b>Nama Grup:</b> {chat.title or '-'}\n"
        f"🆔 <b>ID Grup:</b> <code>{chat.id}</code>\n"
        f"👤 <b>Jumlah Member:</b> {member_count}"
    )
    await update.message.reply_text(text, parse_mode="HTML")


async def linkchannel_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if CREATOR_CHANNEL_LINK:
        text = (
            f"👾 <b>Channel Wajib:</b>\n"
            f"Bergabunglah ke [Channel Ini]({CREATOR_CHANNEL_LINK}) untuk akses penuh ke fitur bot!"
        )
        await update.message.reply_text(text, parse_mode="HTML", disable_web_page_preview=True)
    else:
        await update.message.reply_text("Channel creator belum diatur di bot ini.")


async def support_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🤝 <b>Butuh bantuan atau ingin melaporkan bug?</b>\n"
        "Hubungi kami melalui:\n\n"
        "Telegram: @aesneverhere\n"
        "GitHub: https://github.com/aes-co/MaestroBot"
    )
    await update.message.reply_text(text, parse_mode="HTML")


async def donate_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if DONATION_LINK:
        text = (
            f"💖 <b>Dukung pengembangan MaestroBot!</b>\n"
            f"Kamu bisa berdonasi melalui link berikut:\n{DONATION_LINK}"
        )
        await update.message.reply_text(text, parse_mode="HTML")
    else:
        await update.message.reply_text("Belum ada link donasi yang diatur.")


def register(app):
    app.add_handler(CommandHandler("id", id_command))
    app.add_handler(CommandHandler("userinfo", userinfo_command))
    app.add_handler(CommandHandler("groupinfo", groupinfo_command))
    app.add_handler(CommandHandler("linkchannel", linkchannel_command))
    app.add_handler(CommandHandler("support", support_command))
    app.add_handler(CommandHandler("donate", donate_command))
