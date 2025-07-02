from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from maestrobot.configs import OWNER_ID, SUDO_USERS
from maestrobot.db import settings as db_settings

SETTINGS_TEXT = (
    "⚙️ <b>Pengaturan MaestroBot</b>\n\n"
    "• <b>Channel Wajib:</b> {channel}\n"
    "• <b>Donasi:</b> {donasi}\n"
    "• <b>Mode Musik:</b> {mode_musik}\n"
    "• <b>Welcome Message:</b> {welcome}\n"
    "• <b>Rules:</b> {rules}\n"
    "• <b>Logging:</b> {logging}\n"
    "• <b>Owner:</b> <code>{owner}</code>\n\n"
    "Pilih menu di bawah untuk mengatur pengaturan 👇"
)

def get_settings_keyboard():
    buttons = [
        [
            InlineKeyboardButton("🔗 Channel Wajib", callback_data="edit_channel"),
            InlineKeyboardButton("💖 Link Donasi", callback_data="edit_donasi"),
        ],
        [
            InlineKeyboardButton("🎵 Mode Musik", callback_data="edit_mode_musik"),
            InlineKeyboardButton("👋 Welcome", callback_data="edit_welcome"),
        ],
        [
            InlineKeyboardButton("📜 Rules", callback_data="edit_rules"),
            InlineKeyboardButton("📝 Logging", callback_data="edit_logging"),
        ],
        [
            InlineKeyboardButton("🔄 Refresh", callback_data="refresh_settings"),
            InlineKeyboardButton("❌ Tutup", callback_data="close_settings"),
        ]
    ]
    return InlineKeyboardMarkup(buttons)

async def settings_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    owner = OWNER_ID or "<i>Belum diatur</i>"
    # Ambil setting dari database, fallback default jika belum ada
    channel = await db_settings.get_setting(chat_id, "channel", "<i>Belum diatur</i>")
    donasi = await db_settings.get_setting(chat_id, "donasi", "<i>Belum diatur</i>")
    mode_musik = await db_settings.get_setting(chat_id, "mode_musik", "<i>Belum diatur</i>")
    welcome = await db_settings.get_setting(chat_id, "welcome", "<i>Belum diatur</i>")
    rules = await db_settings.get_setting(chat_id, "rules", "<i>Belum diatur</i>")
    logging = await db_settings.get_setting(chat_id, "logging", "<i>Belum diatur</i>")

    text = SETTINGS_TEXT.format(
        channel=channel, donasi=donasi, mode_musik=mode_musik,
        welcome=welcome, rules=rules, logging=logging, owner=owner
    )
    if update.message:
        await update.message.reply_text(text, reply_markup=get_settings_keyboard(), parse_mode="HTML")
    else:
        await update.callback_query.edit_message_text(text, reply_markup=get_settings_keyboard(), parse_mode="HTML")

def can_edit(update: Update):
    user = update.effective_user
    chat = update.effective_chat
    is_owner = str(user.id) == str(OWNER_ID)
    is_sudo = user.id in SUDO_USERS
    is_admin = False
    if chat.type in ["group", "supergroup"]:
        member = chat.get_member(user.id)
        is_admin = member.status in ["administrator", "creator"]
    return is_owner or is_sudo or is_admin

async def settings_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = query.data

    # Tutup menu
    if data == "close_settings":
        await query.message.delete()
        return

    # Refresh menu
    if data == "refresh_settings":
        await settings_menu(update, context)
        await query.answer("Pengaturan di-refresh!")
        return

    # Edit channel wajib
    if data == "edit_channel":
        if not can_edit(update):
            await query.answer("Hanya owner/sudo/admin yang bisa ubah setting ini!", show_alert=True)
            return
        await query.answer()
        await query.message.reply_text(
            "Masukkan link channel wajib baru (atau ketik /cancel untuk batal):"
        )
        context.user_data["edit_setting"] = "channel"
        return

    # Edit link donasi
    if data == "edit_donasi":
        if not can_edit(update):
            await query.answer("Hanya owner/sudo/admin yang bisa ubah setting ini!", show_alert=True)
            return
        await query.answer()
        await query.message.reply_text(
            "Masukkan link donasi baru (atau ketik /cancel untuk batal):"
        )
        context.user_data["edit_setting"] = "donasi"
        return

    # Edit mode musik
    if data == "edit_mode_musik":
        if not can_edit(update):
            await query.answer("Hanya owner/sudo/admin yang bisa ubah setting ini!", show_alert=True)
            return
        await query.answer()
        buttons = [
            [
                InlineKeyboardButton("Grup & Channel", callback_data="set_mode_musik|Grup & Channel"),
                InlineKeyboardButton("Grup Saja", callback_data="set_mode_musik|Grup Saja"),
                InlineKeyboardButton("Channel Saja", callback_data="set_mode_musik|Channel Saja"),
            ]
        ]
        await query.message.reply_text(
            "Pilih mode musik yang diizinkan:",
            reply_markup=InlineKeyboardMarkup(buttons)
        )
        return

    # Edit welcome
    if data == "edit_welcome":
        if not can_edit(update):
            await query.answer("Hanya owner/sudo/admin yang bisa ubah setting ini!", show_alert=True)
            return
        await query.answer()
        buttons = [
            [
                InlineKeyboardButton("Aktif", callback_data="set_welcome|Aktif"),
                InlineKeyboardButton("Nonaktif", callback_data="set_welcome|Nonaktif"),
            ]
        ]
        await query.message.reply_text(
            "Aktifkan/padamkan pesan welcome?",
            reply_markup=InlineKeyboardMarkup(buttons)
        )
        return

    # Edit rules
    if data == "edit_rules":
        if not can_edit(update):
            await query.answer("Hanya owner/sudo/admin yang bisa ubah setting ini!", show_alert=True)
            return
        await query.answer()
        await query.message.reply_text(
            "Kirim rules grup baru (atau ketik /cancel untuk batal):"
        )
        context.user_data["edit_setting"] = "rules"
        return

    # Edit logging
    if data == "edit_logging":
        if not can_edit(update):
            await query.answer("Hanya owner/sudo/admin yang bisa ubah setting ini!", show_alert=True)
            return
        await query.answer()
        buttons = [
            [
                InlineKeyboardButton("Aktif", callback_data="set_logging|Aktif"),
                InlineKeyboardButton("Nonaktif", callback_data="set_logging|Nonaktif"),
            ]
        ]
        await query.message.reply_text(
            "Aktifkan logging aktivitas bot di grup ini?",
            reply_markup=InlineKeyboardMarkup(buttons)
        )
        return

    # Callback set value (mode_musik, welcome, logging)
    if data.startswith("set_mode_musik|"):
        val = data.split("|", 1)[1]
        chat_id = update.effective_chat.id
        await db_settings.set_setting(chat_id, "mode_musik", val)
        await query.answer(f"Mode musik diubah ke: {val}")
        await settings_menu(update, context)
        return

    if data.startswith("set_welcome|"):
        val = data.split("|", 1)[1]
        chat_id = update.effective_chat.id
        await db_settings.set_setting(chat_id, "welcome", val)
        await query.answer(f"Welcome diubah ke: {val}")
        await settings_menu(update, context)
        return

    if data.startswith("set_logging|"):
        val = data.split("|", 1)[1]
        chat_id = update.effective_chat.id
        await db_settings.set_setting(chat_id, "logging", val)
        await query.answer(f"Logging diubah ke: {val}")
        await settings_menu(update, context)
        return

    await query.answer("Fitur edit belum tersedia/invalid callback.", show_alert=True)

# Handler pesan untuk input manual (channel, donasi, rules)
async def handle_setting_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    if "edit_setting" not in context.user_data:
        return
    key = context.user_data.pop("edit_setting")
    value = update.message.text.strip()
    if value.lower() == "/cancel":
        await update.message.reply_text("Edit pengaturan dibatalkan.")
        return
    await db_settings.set_setting(chat_id, key, value)
    await update.message.reply_text(f"Pengaturan <b>{key}</b> diubah ke:\n{value}", parse_mode="HTML")
    await settings_menu(update, context)

def setup(dispatcher):
    dispatcher.add_handler(CommandHandler(["settings", "pengaturan"], settings_menu))
    dispatcher.add_handler(CallbackQueryHandler(settings_callback, pattern="^(edit_channel|edit_donasi|edit_mode_musik|edit_welcome|edit_rules|edit_logging|set_mode_musik\\|.*|set_welcome\\|.*|set_logging\\|.*|refresh_settings|close_settings)$"))
    dispatcher.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_setting_input))