from telegram import Update
from telegram.ext import ContextTypes

from bot.keyboards import main_menu_keyboard
from utils.link_validator import TikTokLinkValidator
from services.tiktok_downloader import TikTokDownloader, DownloadError
from storage.history_storage import HistoryStorage


validator = TikTokLinkValidator()
downloader = TikTokDownloader()
history_storage = HistoryStorage()


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Hello! I am TikTok Video Helper Bot.\n\n"
        "Send me a public TikTok video link, and I will try to download it."
    )

    await update.message.reply_text(
        text,
        reply_markup=main_menu_keyboard()
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "How to use this bot:\n\n"
        "1. Send a public TikTok video link.\n"
        "2. Wait while the bot downloads the video.\n"
        "3. The bot will send the video back to you.\n"
        "4. Use /history to see your download history.\n"
        "5. Use /clear_history to delete your history.\n\n"
        "Only public TikTok links are supported."
    )

    await update.message.reply_text(text)


async def history_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    history = history_storage.get_history(user_id)

    if not history:
        await update.message.reply_text("Your download history is empty.")
        return

    text = "Your download history:\n\n"

    for index, item in enumerate(history[-5:], start=1):
        text += (
            f"{index}. {item['url']}\n"
            f"Date: {item['downloaded_at']}\n\n"
        )

    await update.message.reply_text(text)


async def clear_history_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    history_storage.clear_history(user_id)

    await update.message.reply_text("Your download history has been cleared.")


async def text_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    user_id = update.effective_user.id

    if not validator.is_tiktok_link(user_text):
        await update.message.reply_text(
            "Please send a valid TikTok video link."
        )
        return

    await update.message.reply_text("TikTok link detected ✅\nDownloading video...")

    try:
        video_path = downloader.download(user_text)

        history_storage.add_download(
            user_id=user_id,
            url=user_text,
            file_path=video_path
        )

        with open(video_path, "rb") as video:
            await update.message.reply_video(video=video)

    except DownloadError as error:
        await update.message.reply_text(
            "Sorry, I could not download this video.\n\n"
            f"Reason: {error}"
        )

    except Exception as error:
        await update.message.reply_text(
            "Unexpected error happened. Please try again later.\n\n"
            f"Reason: {error}"
        )