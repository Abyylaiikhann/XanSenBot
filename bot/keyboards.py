from telegram import ReplyKeyboardMarkup


def main_menu_keyboard():
    keyboard = [
        ["/help", "/history"],
        ["/clear_history"]
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )