from telegram import Update
from telegram.ext import ContextTypes

from bot.keyboards import main_menu_keyboard
from utils.link_validator import TikTokLinkValidator
from services.tiktok_downloader import TikTokDownloader, DownloadError


validator = TikTokLinkValidator()
downloader = TikTokDownloader()


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
        "3. The bot will send the video back to you.\n\n"
        "Only public TikTok links are supported."
    )

    await update.message.reply_text(text)


async def text_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    if not validator.is_tiktok_link(user_text):
        await update.message.reply_text(
            "Please send a valid TikTok video link."
        )
        return

    await update.message.reply_text("TikTok link detected ✅\nDownloading video...")

    try:
        video_path = downloader.download(user_text)

        with open(video_path, "rb") as video:
            await update.message.reply_video(video=video)

    except DownloadError:
        await update.message.reply_text(
            "Sorry, I could not download this video.\n"
            "Please check if the TikTok link is public and correct."
        )

    except Exception:
        await update.message.reply_text(
            "Unexpected error happened. Please try again later."
        )