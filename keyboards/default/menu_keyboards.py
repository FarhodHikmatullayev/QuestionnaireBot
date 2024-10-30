from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

back_to_menu = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="🔙 Bosh Menyu"),
        ]
    ]
)

menu_default_keyboard_for_admin = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="📝 Atvet yuborish"),
        ],
        [
            KeyboardButton(text="📥 Javoblarni yuklab olish")
        ]

    ]
)

menu_default_keyboard_for_users = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="Atvet 📝 Atvet yuborish"),
        ],
    ]
)
