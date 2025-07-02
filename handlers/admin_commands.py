from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
from maestrobot.player.player_manager import (
    mute_voice_chat,
    unmute_voice_chat,
    kick_from_voice_chat,
)
from maestrobot.db.settings import add_sudo_user, remove_sudo_user, get_sudo_users
from maestrobot.configs import OWNER_ID

def is_owner_or_sudo(user_id):
    sudo_users = []
    try:
        # get_sudo_users is async, but this will be awaited in handler
        sudo_users = get_sudo_users()
    except Exception:
        pass
    return user_id == int(OWNER_ID) or user_id in sudo_users

async def mute_command(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    await mute_voice_chat(chat_id)
    await update.message.reply_text("🔇 Semua peserta VC dimute.")

async def unmute_command(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    await unmute_voice_chat(chat_id)
    await update.message.reply_text("🔊 Semua peserta VC diunmute.")

async def kickvc_command(update: Update, context: CallbackContext):
    if not context.args or not context.args[0].isdigit():
        await update.message.reply_text("Kirim: /kickvc <user_id>")
        return
    chat_id = update.effective_chat.id
    user_id = int(context.args[0])
    await kick_from_voice_chat(chat_id, user_id)
    await update.message.reply_text(f"🚫 User {user_id} dikeluarkan dari VC.")

async def sudo_add_command(update: Update, context: CallbackContext):
    if not context.args or not context.args[0].isdigit():
        await update.message.reply_text("Kirim: /addsudo <user_id>")
        return
    user_id = int(context.args[0])
    await add_sudo_user(user_id)
    await update.message.reply_text(f"✅ User {user_id} ditambahkan sebagai sudo.")

async def sudo_remove_command(update: Update, context: CallbackContext):
    if not context.args or not context.args[0].isdigit():
        await update.message.reply_text("Kirim: /delsudo <user_id>")
        return
    user_id = int(context.args[0])
    await remove_sudo_user(user_id)
    await update.message.reply_text(f"❌ User {user_id} dihapus dari sudo.")

async def sudo_list_command(update: Update, context: CallbackContext):
    sudos = await get_sudo_users()
    if not sudos:
        await update.message.reply_text("Belum ada sudo user.")
        return
    text = "👑 Daftar sudo user:\n"
    for uid in sudos:
        text += f"- <code>{uid}</code>\n"
    await update.message.reply_text(text, parse_mode="HTML")

def setup(dispatcher):
    dispatcher.add_handler(CommandHandler("mutevc", mute_command))
    dispatcher.add_handler(CommandHandler("unmutevc", unmute_command))
    dispatcher.add_handler(CommandHandler("kickvc", kickvc_command))
    dispatcher.add_handler(CommandHandler("addsudo", sudo_add_command))
    dispatcher.add_handler(CommandHandler("delsudo", sudo_remove_command))
    dispatcher.add_handler(CommandHandler("sudolist", sudo_list_command))