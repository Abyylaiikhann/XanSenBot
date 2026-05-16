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
        "Welcome to TikTok Video Helper Bot 👋\n\n"
        "Send me a public TikTok video link, and I will try to download it for you.\n\n"
        "You can also use:\n"
        "/help — how to use the bot\n"
        "/history — view your recent downloads\n"
        "/clear_history — clear your download history"
    )

    await update.message.reply_text(
        text,
        reply_markup=main_menu_keyboard()
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "How to use this bot:\n\n"
        "1. Copy a public TikTok video link.\n"
        "2. Send the link to this chat.\n"
        "3. Wait while the bot downloads the video.\n"
        "4. The bot will send the video back to you.\n\n"
        "Supported links:\n"
        "- https://www.tiktok.com/...\n"
        "- https://vt.tiktok.com/...\n"
        "- https://vm.tiktok.com/...\n\n"
        "Note: Private or restricted videos may not work."
    )

    await update.message.reply_text(text)


async def history_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    history = history_storage.get_history(user_id)

    if not history:
        await update.message.reply_text(
            "Your download history is empty.\n"
            "Send a TikTok link first, then check /history again."
        )
        return

    text = "Your recent download history:\n\n"

    for index, item in enumerate(history[-5:], start=1):
        text += (
            f"{index}. {item['url']}\n"
            f"Date: {item['downloaded_at']}\n\n"
        )

    await update.message.reply_text(text)


async def clear_history_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    history_storage.clear_history(user_id)

    await update.message.reply_text(
        "Your download history has been cleared ✅"
    )


async def text_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    user_id = update.effective_user.id

    if not validator.is_tiktok_link(user_text):
        await update.message.reply_text(
            "This does not look like a TikTok link.\n"
            "Please send a valid public TikTok video link."
        )
        return

    await update.message.reply_text(
        "TikTok link detected ✅\n"
        "Downloading video, please wait..."
    )

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
            "Possible reasons:\n"
            "- the video is private\n"
            "- the link is restricted\n"
            "- TikTok blocked the request\n\n"
            f"Technical reason: {error}"
        )

    except Exception as error:
        await update.message.reply_text(
            "Unexpected error happened. Please try again later.\n\n"
            f"Technical reason: {error}"
        )