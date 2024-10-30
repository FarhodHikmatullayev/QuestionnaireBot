from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from keyboards.default.menu_keyboards import menu_default_keyboard_for_admin, menu_default_keyboard_for_users
from loader import dp, db, bot


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message, state: FSMContext):
    user_telegram_id = message.from_user.id
    full_name = message.from_user.full_name
    username = message.from_user.username
    users = await db.select_users(telegram_id=user_telegram_id)
    if not users:
        user = await db.create_user(
            username=username,
            full_name=full_name,
            telegram_id=user_telegram_id,
        )

    if str(user_telegram_id) in ADMINS:
        await message.reply(
            text=f"👋 Salom, {full_name}\n"
                 f"📋 So'rovnomada ishtirok etish uchun, '📝 Atvet yuborish' tugmasini bosing.",
            reply_markup=menu_default_keyboard_for_admin
        )
    else:
        await message.reply(
            text=f"👋 Salom, {full_name}\n"
                 f"📋 So'rovnomada ishtirok etish uchun, '📝 Atvet yuborish' tugmasini bosing.",
            reply_markup=menu_default_keyboard_for_users
        )
