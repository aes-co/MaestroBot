from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from maestrobot.configs import OWNER_ID, SUDO_USERS
from maestrobot.db import settings as db_settings

SETTINGS_TEXT = (
    "\u2699\ufe0f <b>Pengaturan MaestroBot</b>\n\n"
    "\u2022 <b>Channel Wajib:</b> {channel}\n"
    "\u2022 <b>Donasi:</b> {donasi}\n"
    "\u2022 <b>Mode Musik:</b> {mode_musik}\n"
    "\u2022 <b>Welcome Message:</b> {welcome}\n"
    "\u2022 <b>Rules:</b> {rules}\n"
    "\u2022 <b>Logging:</b> {logging}\n"
    "\u2022 <b>Owner:</b> <code>{owner}</code>\n\n"
    "Pilih menu di bawah untuk mengatur pengaturan \ud83d\udc47"
)

def get_settings_keyboard():
    buttons = [
        [
            InlineKeyboardButton("\ud83d\udd17 Channel Wajib", callback_data="edit_channel"),
            InlineKeyboardButton("\ud83d\udc96 Link Donasi", callback_data="edit_donasi"),
        ],
        [
            InlineKeyboardButton("\ud83c\udfb5 Mode Musik", callback_data="edit_mode_musik"),
            InlineKeyboardButton("\ud83d\udc4b Welcome", callback_data="edit_welcome"),
        ],
        [
            InlineKeyboardButton("\ud83d\udcdc Rules", callback_data="edit_rules"),
            InlineKeyboardButton("\ud83d\udcdd Logging", callback_data="edit_logging"),
        ],
        [
            InlineKeyboardButton("\ud83d\udd04 Refresh", callback_data="refresh_settings"),
            InlineKeyboardButton("\u274c Tutup", callback_data="close_settings"),
        ]
    ]
    return InlineKeyboardMarkup(buttons)

async def settings_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    owner = OWNER_ID or "<i>Belum diatur</i>"
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

    if data == "close_settings":
        await query.message.delete()
        return

    if data == "refresh_settings":
        await settings_menu(update, context)
        await query.answer("Pengaturan di-refresh!")
        return

    if data == "edit_channel":
        if not can_edit(update):
            await query.answer("Hanya owner/sudo/admin yang bisa ubah setting ini!", show_alert=True)
            return
        await query.answer()
        await query.message.reply_text("Masukkan link channel wajib baru (atau ketik /cancel untuk batal):")
        context.user_data["edit_setting"] = "channel"
        return

    if data == "edit_donasi":
        if not can_edit(update):
            await query.answer("Hanya owner/sudo/admin yang bisa ubah setting ini!", show_alert=True)
            return
        await query.answer()
        await query.message.reply_text("Masukkan link donasi baru (atau ketik /cancel untuk batal):")
        context.user_data["edit_setting"] = "donasi"
        return

    if data == "edit_mode_musik":
        if not can_edit(update):
            await query.answer("Hanya owner/sudo/admin yang bisa ubah setting ini!", show_alert=True)
            return
        await query.answer()
        buttons = [[
            InlineKeyboardButton("Grup & Channel", callback_data="set_mode_musik|Grup & Channel"),
            InlineKeyboardButton("Grup Saja", callback_data="set_mode_musik|Grup Saja"),
            InlineKeyboardButton("Channel Saja", callback_data="set_mode_musik|Channel Saja")
        ]]
        await query.message.reply_text("Pilih mode musik yang diizinkan:", reply_markup=InlineKeyboardMarkup(buttons))
        return

    if data == "edit_welcome":
        if not can_edit(update):
            await query.answer("Hanya owner/sudo/admin yang bisa ubah setting ini!", show_alert=True)
            return
        await query.answer()
        buttons = [[
            InlineKeyboardButton("Aktif", callback_data="set_welcome|Aktif"),
            InlineKeyboardButton("Nonaktif", callback_data="set_welcome|Nonaktif")
        ]]
        await query.message.reply_text("Aktifkan/padamkan pesan welcome?", reply_markup=InlineKeyboardMarkup(buttons))
        return

    if data == "edit_rules":
        if not can_edit(update):
            await query.answer("Hanya owner/sudo/admin yang bisa ubah setting ini!", show_alert=True)
            return
        await query.answer()
        await query.message.reply_text("Kirim rules grup baru (atau ketik /cancel untuk batal):")
        context.user_data["edit_setting"] = "rules"
        return

    if data == "edit_logging":
        if not can_edit(update):
            await query.answer("Hanya owner/sudo/admin yang bisa ubah setting ini!", show_alert=True)
            return
        await query.answer()
        buttons = [[
            InlineKeyboardButton("Aktif", callback_data="set_logging|Aktif"),
            InlineKeyboardButton("Nonaktif", callback_data="set_logging|Nonaktif")
        ]]
        await query.message.reply_text("Aktifkan logging aktivitas bot di grup ini?", reply_markup=InlineKeyboardMarkup(buttons))
        return

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

handlers = [
    CommandHandler(["settings", "pengaturan"], settings_menu),
    CallbackQueryHandler(settings_callback, pattern="^(edit_channel|edit_donasi|edit_mode_musik|edit_welcome|edit_rules|edit_logging|set_mode_musik\\|.*|set_welcome\\|.*|set_logging\\|.*|refresh_settings|close_settings)$"),
    MessageHandler(filters.TEXT & ~filters.COMMAND, handle_setting_input)
]
