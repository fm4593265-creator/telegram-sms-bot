import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler

TOKEN = os.environ.get("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable is missing")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📩 الرسائل", callback_data="messages")],
        [InlineKeyboardButton("ℹ️ المساعدة", callback_data="help")],
    ]
    await update.message.reply_text(
        "أهلاً بك 👋\nاختاري من القائمة:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "messages":
        await query.edit_message_text(
            "📩 قسم الرسائل\n\nسيتم ربطه بمنصة الـSMS لاحقاً."
        )
    elif query.data == "help":
        await query.edit_message_text(
            "ℹ️ الأوامر المتاحة:\n/start — تشغيل البوت\n/help — المساعدة"
        )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start — تشغيل البوت\n/help — عرض المساعدة"
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CallbackQueryHandler(buttons))
    app.run_polling()

if __name__ == "__main__":
    main()
