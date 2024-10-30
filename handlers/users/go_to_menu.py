from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import ADMINS
from keyboards.default.menu_keyboards import menu_default_keyboard_for_users, menu_default_keyboard_for_admin, \
    back_to_menu
from loader import dp, db, bot


@dp.message_handler(text='🔙 Bosh Menyu', state='*')
async def go_to_menu_function(message: types.Message, state: FSMContext):
    try:
        await state.finish()
    except:
        pass
    user_telegram_id = message.from_user.id

    if str(user_telegram_id) in ADMINS:
        await message.reply(
            text=f"📋 So'rovnomada ishtirok etish uchun, '📝 Atvet yuborish' tugmasini bosing.",
            reply_markup=menu_default_keyboard_for_admin
        )
    else:
        await message.reply(
            text=f"📋 So'rovnomada ishtirok etish uchun, '📝 Atvet yuborish' tugmasini bosing.",
            reply_markup=menu_default_keyboard_for_users
        )
