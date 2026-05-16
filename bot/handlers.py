from telegram import Update
from telegram.ext import ContextTypes
from bot.keyboards import main_menu_keyboard


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Hello! I am TikTok Video Helper Bot.\n\n"
        "Send me a public TikTok video link, and I will try to process it."
    )

    await update.message.reply_text(
        text,
        reply_markup=main_menu_keyboard()
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "How to use this bot:\n\n"
        "1. Send a TikTok video link.\n"
        "2. Wait while the bot processes it.\n"
        "3. Use /history to see your saved links.\n\n"
        "Only public TikTok links are supported."
    )

    await update.message.reply_text(text)


async def text_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    await update.message.reply_text(
        f"You sent:\n{user_text}\n\n"
        "TikTok link processing will be added in the next commits."
    )