from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import db


async def all_branches_default_keyboard():
    branches = await db.select_all_branches()
    markup = ReplyKeyboardMarkup()
    markup.resize_keyboard = True
    markup.row_width = 1
    for branch in branches:
        text_button = branch['name']
        markup.insert(KeyboardButton(text_button))

    markup.insert(KeyboardButton(text="🔙 Bosh Menyu"))

    return markup
