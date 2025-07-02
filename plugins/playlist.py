from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
from maestrobot.db.playlists import (
    save_playlist,
    get_playlists,
    get_playlist,
    delete_playlist
)
from maestrobot.player import get_current_queue, add_to_queue

async def saveplaylist_command(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if not context.args:
        await update.message.reply_text("Kirim: /saveplaylist <nama_playlist>")
        return

    name = context.args[0].lower()
    queue = get_current_queue(update.effective_chat.id)
    if not queue:
        await update.message.reply_text("Tidak ada lagu dalam antrian.")
        return

    await save_playlist(user_id, name, queue)
    await update.message.reply_text(f"✅ Playlist '{name}' berhasil disimpan!")

async def myplaylist_command(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    playlists = await get_playlists(user_id)
    if not playlists:
        await update.message.reply_text("Kamu belum menyimpan playlist apa pun.")
        return

    text = "📂 Playlist kamu:\n\n"
    for name, tracks in playlists.items():
        text += f"• <b>{name}</b> ({len(tracks)} lagu)\n"
    await update.message.reply_text(text, parse_mode="HTML")

async def playplaylist_command(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id
    if not context.args:
        await update.message.reply_text("Kirim: /playplaylist <nama_playlist>")
        return

    name = context.args[0].lower()
    tracks = await get_playlist(user_id, name)
    if not tracks:
        await update.message.reply_text("Playlist tidak ditemukan atau kosong.")
        return

    for track in tracks:
        await add_to_queue(chat_id, track)
    await update.message.reply_text(f"▶️ Memutar playlist '{name}' ({len(tracks)} lagu).")

async def delplaylist_command(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if not context.args:
        await update.message.reply_text("Kirim: /delplaylist <nama_playlist>")
        return

    name = context.args[0].lower()
    ok = await delete_playlist(user_id, name)
    if not ok:
        await update.message.reply_text("Gagal menghapus playlist atau tidak ditemukan.")
    else:
        await update.message.reply_text(f"🗑 Playlist '{name}' dihapus.")

def setup(dispatcher):
    dispatcher.add_handler(CommandHandler("saveplaylist", saveplaylist_command))
    dispatcher.add_handler(CommandHandler("myplaylist", myplaylist_command))
    dispatcher.add_handler(CommandHandler("playplaylist", playplaylist_command))
    dispatcher.add_handler(CommandHandler("delplaylist", delplaylist_command))
