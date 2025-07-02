from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CommandHandler, CallbackQueryHandler
from maestrobot.configs import CREATOR_CHANNEL_LINK, DONATION_LINK

START_TEXT = (
    "🎷 <b>Welcome to MaestroBot!</b>\n\n"
    "Hai {mention} 👋, siap putar musik berkualitas di grup kamu?\n"
    "Aku bisa temenin kamu dengerin lagu, karaokean, sampai atur antrian musik di voice chat Telegram!\n\n"
    "🔹 <b>Fitur utama:</b>\n"
    "• Streaming musik real-time di voice chat\n"
    "• Kontrol interaktif langsung dari chat (pause, skip, volume, dsb)\n"
    "• Cari lirik otomatis, rekomendasi lagu, & lebih banyak lagi\n"
    "• Bisa di group, channel, bahkan ada web app-nya juga lho!\n\n"
    "Yuk mulai dengan /play <judul/tautan> atau cek menu bantuan di bawah 👇"
)

HELP_TEXT = (
    "📝 <b>Panduan Singkat MaestroBot</b>\n\n"
    "📀 <b>Music</b>\n"
    "<code>/play &lt;judul/tautan&gt;</code> — Putar musik dari Youtube/Spotify dll\n"
    "<code>/queue</code> — Lihat antrian lagu\n"
    "<code>/nowplaying</code> — Info lagu yang sedang diputar\n"
    "<code>/pause</code> <code>/resume</code> <code>/skip</code> <code>/stop</code> — Kontrol playback\n"
    "<code>/lyrics</code> — Cari lirik lagu\n"
    "<code>/volume &lt;0-200&gt;</code> — Atur volume\n"
    "<code>/quality &lt;low/medium/high&gt;</code> — Pilih kualitas audio\n\n"
    "🛠️ <b>Setting & Admin</b>\n"
    "<code>/bs</code> <code>/bset</code> <code>/botsetting</code> — Buka menu pengaturan bot\n"
    "<code>/admins</code> — Lihat admin grup\n"
    "<code>/mute</code> <code>/unmute</code> <code>/kick</code> — Moderasi VC\n\n"
    "💡 <b>Lainnya</b>\n"
    "<code>/support</code> — Info support, bug report\n"
    "<code>/donate</code> — Dukung pengembangan bot 💖\n"
    "<code>/id</code> <code>/userinfo</code> — Lihat info user/grup\n\n"
    "Punya pertanyaan? Join support channel atau klik tombol di bawah ini ya! 👇"
)

def get_buttons():
    buttons = [[
        InlineKeyboardButton("🎶 Mulai Putar Musik", switch_inline_query_current_chat=""),
        InlineKeyboardButton("ℹ️ Bantuan", callback_data="open_help")
    ]]
    row2 = []
    if CREATOR_CHANNEL_LINK:
        row2.append(InlineKeyboardButton("👾 Channel Creator", url=CREATOR_CHANNEL_LINK))
    if DONATION_LINK:
        row2.append(InlineKeyboardButton("💖 Donasi", url=DONATION_LINK))
    if row2:
        buttons.append(row2)
    return InlineKeyboardMarkup(buttons)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        START_TEXT.format(mention=user.mention_html()),
        reply_markup=get_buttons(),
        parse_mode="HTML"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        HELP_TEXT,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 Kembali", callback_data="start_menu")]
        ]),
        parse_mode="HTML"
    )

async def start_help_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = query.data

    if data == "open_help":
        await query.answer()
        await query.message.edit_text(HELP_TEXT, parse_mode="HTML")

    elif data == "start_menu":
        user = update.effective_user
        await query.answer()
        await query.message.edit_text(
            START_TEXT.format(mention=user.mention_html()),
            reply_markup=get_buttons(),
            parse_mode="HTML"
        )

handlers = [
    CommandHandler("start", start_command),
    CommandHandler("help", help_command),
    CallbackQueryHandler(start_help_callback, pattern="^(open_help|start_menu)$")
]
