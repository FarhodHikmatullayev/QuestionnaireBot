from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import db


async def all_ranks_default_keyboard():
    ranks = await db.select_all_ranks()
    markup = ReplyKeyboardMarkup()
    markup.resize_keyboard = True
    markup.row_width = 2
    for branch in ranks:
        text_button = branch['name']
        markup.insert(KeyboardButton(text_button))

    markup.insert(KeyboardButton(text="🔙 Bosh Menyu"))

    return markup
