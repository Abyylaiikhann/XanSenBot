from telegram.ext import Application, CommandHandler, MessageHandler, filters

from config import BOT_TOKEN
from bot.handlers import (
    start_command,
    help_command,
    history_command,
    clear_history_command,
    text_message
)


def main():
    if not BOT_TOKEN:
        print("Error: BOT_TOKEN is missing. Please add it to .env file.")
        return

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("history", history_command))
    app.add_handler(CommandHandler("clear_history", clear_history_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_message))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()