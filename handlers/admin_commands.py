from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from maestrobot.player.player_manager import (
    mute_voice_chat,
    unmute_voice_chat,
    kick_from_voice_chat,
)
from maestrobot.db.settings import (
    add_sudo_user,
    remove_sudo_user,
    get_sudo_users,
)
from maestrobot.configs import OWNER_ID


async def mutevc_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await mute_voice_chat(chat_id)
    await update.message.reply_text("🔇 Semua peserta VC dimute.")


async def unmutevc_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await unmute_voice_chat(chat_id)
    await update.message.reply_text("🔊 Semua peserta VC diunmute.")


async def kickvc_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args or not context.args[0].isdigit():
        await update.message.reply_text("Kirim: /kickvc <user_id>")
        return
    chat_id = update.effective_chat.id
    user_id = int(context.args[0])
    await kick_from_voice_chat(chat_id, user_id)
    await update.message.reply_text(f"🚫 User {user_id} dikeluarkan dari VC.")


async def addsudo_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args or not context.args[0].isdigit():
        await update.message.reply_text("Kirim: /addsudo <user_id>")
        return
    user_id = int(context.args[0])
    await add_sudo_user(user_id)
    await update.message.reply_text(f"✅ User {user_id} ditambahkan sebagai sudo.")


async def delsudo_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args or not context.args[0].isdigit():
        await update.message.reply_text("Kirim: /delsudo <user_id>")
        return
    user_id = int(context.args[0])
    await remove_sudo_user(user_id)
    await update.message.reply_text(f"❌ User {user_id} dihapus dari sudo.")


async def sudolist_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sudos = await get_sudo_users()
    if not sudos:
        await update.message.reply_text("Belum ada sudo user.")
        return
    text = "👑 Daftar sudo user:\n"
    for uid in sudos:
        text += f"- <code>{uid}</code>\n"
    await update.message.reply_text(text, parse_mode="HTML")


handlers = [
    CommandHandler("mutevc", mutevc_command),
    CommandHandler("unmutevc", unmutevc_command),
    CommandHandler("kickvc", kickvc_command),
    CommandHandler("addsudo", addsudo_command),
    CommandHandler("delsudo", delsudo_command),
    CommandHandler("sudolist", sudolist_command),
]
