from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.all_branches import all_branches_default_keyboard
from keyboards.default.all_ranks import all_ranks_default_keyboard
from keyboards.default.menu_keyboards import back_to_menu
from keyboards.inline.confirmation import confirm_keyboard
from keyboards.inline.mark_keyboards import marks_keyboard
from loader import dp, db, bot
from states.questionnaire_states import CreateQuestionnaireState


@dp.message_handler(text="📝 Atvet yuborish", state="*")
async def get_branch(message: types.Message, state: FSMContext):
    try:
        await state.finish()
    except:
        pass
    markup = await all_branches_default_keyboard()
    await message.answer(text="🏢 So'rovnomani to'ldirish uchun filialni tanlang:", reply_markup=markup)
    await CreateQuestionnaireState.branch_id.set()
    user_telegram_id = message.from_user.id
    users = await db.select_users(telegram_id=user_telegram_id)
    if users:
        await state.update_data(user_id=users[0]['id'])
    else:
        username = await message.from_user.username
        full_name = await message.from_user.full_name
        user = await db.create_user(
            username=username,
            full_name=full_name,
            telegram_id=user_telegram_id,
        )
        await state.update_data(user_id=user['id'])


@dp.message_handler(state=CreateQuestionnaireState.branch_id)
async def get_branch_id(message: types.Message, state: FSMContext):
    branch_name = message.text
    branches = await db.select_branches(name=branch_name)
    if not branches:
        await message.reply(text="❌ Bunday filial topilmadi. 😔", reply_markup=back_to_menu)
        return
    branch = branches[0]
    branch_id = branch['id']
    await state.update_data(branch_id=branch_id)
    markup = await all_ranks_default_keyboard()
    await message.answer(text="📂 Bo'lim (Lavozim)ni tanlang:", reply_markup=markup)
    await CreateQuestionnaireState.rank_id.set()


@dp.message_handler(state=CreateQuestionnaireState.rank_id)
async def get_rank_id(message: types.Message, state: FSMContext):
    rank_name = message.text
    ranks = await db.select_ranks(name=rank_name)
    if not ranks:
        await message.reply(text="❌ Bunday lavozim topilmadi. 😔", reply_markup=back_to_menu)
        return
    rank = ranks[0]
    rank_id = rank['id']
    await state.update_data(rank_id=rank_id)
    await message.answer(
        text="🌍 Ish muhiti va madaniyatiga baho bering:", reply_markup=marks_keyboard
    )
    await CreateQuestionnaireState.ish_muhiti_va_madaniyati.set()


@dp.callback_query_handler(state=CreateQuestionnaireState.ish_muhiti_va_madaniyati)
async def get_mark_for_ish_muhiti_va_madaniyati(call: types.CallbackQuery, state: FSMContext):
    mark = call.data
    mark = int(mark)
    await state.update_data(ish_muhiti_va_madaniyati=mark)
    await call.message.edit_text(
        text="📈 Rivojlanish va o'sish imkoniyatlariga baho bering:", reply_markup=marks_keyboard
    )
    await CreateQuestionnaireState.rivojlanish_va_osish_imkoniyatlari.set()


@dp.callback_query_handler(state=CreateQuestionnaireState.rivojlanish_va_osish_imkoniyatlari)
async def get_mark_for_rivojlanish_va_osish_imkoniyatlari(call: types.CallbackQuery, state: FSMContext):
    mark = call.data
    mark = int(mark)
    await state.update_data(rivojlanish_va_osish_imkoniyatlari=mark)
    await call.message.edit_text(
        text="💰 Ish haqi va mukofotlarga baho bering:", reply_markup=marks_keyboard
    )
    await CreateQuestionnaireState.ish_haqi_va_mukofotlar.set()


@dp.callback_query_handler(state=CreateQuestionnaireState.ish_haqi_va_mukofotlar)
async def get_mark_for_ish_haqi_va_mukofotlar(call: types.CallbackQuery, state: FSMContext):
    mark = call.data
    mark = int(mark)
    await state.update_data(ish_haqi_va_mukofotlar=mark)
    await call.message.edit_text(
        text="👥 Rahbariyat bilan munosabatga baho bering:", reply_markup=marks_keyboard
    )
    await CreateQuestionnaireState.rahbariyat_bilan_munosabat.set()


@dp.callback_query_handler(state=CreateQuestionnaireState.rahbariyat_bilan_munosabat)
async def get_mark_for_rahbariyat_bilan_munosabat(call: types.CallbackQuery, state: FSMContext):
    mark = call.data
    mark = int(mark)
    await state.update_data(rahbariyat_bilan_munosabat=mark)
    await call.message.edit_text(
        text="⚖️ Ish muvozanati va farovonligi (Ish va hayot muvozanatiga e'tibor, stress darajasi, dam olish va tanaffuslar, ish yuklamasi)ga baho bering:",
        reply_markup=marks_keyboard
    )
    await CreateQuestionnaireState.ish_muvozanati_va_farovonligi.set()


@dp.callback_query_handler(text="yes", state=CreateQuestionnaireState.ish_muvozanati_va_farovonligi)
async def save_questionnaire_function(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    user_id = data.get('user_id')
    branch_id = data.get('branch_id')
    rank_id = data.get('rank_id')
    ish_muhiti_va_madaniyati = data.get('ish_muhiti_va_madaniyati')
    rivojlanish_va_osish_imkoniyatlari = data.get('rivojlanish_va_osish_imkoniyatlari')
    ish_haqi_va_mukofotlar = data.get('ish_haqi_va_mukofotlar')
    rahbariyat_bilan_munosabat = data.get('rahbariyat_bilan_munosabat')
    ish_muvozanati_va_farovonligi = data.get('ish_muvozanati_va_farovonligi')

    questionnaire = await db.create_questionnaire(
        user_id=user_id,
        branch_id=branch_id,
        rank_id=rank_id,
        ish_muhiti_va_madaniyati=ish_muhiti_va_madaniyati,
        rivojlanish_va_osish_imkoniyatlari=rivojlanish_va_osish_imkoniyatlari,
        ish_haqi_va_mukofotlar=ish_haqi_va_mukofotlar,
        rahbariyat_bilan_munosabat=rahbariyat_bilan_munosabat,
        ish_muvozanati_va_farovonligi=ish_muvozanati_va_farovonligi
    )
    await call.message.answer(text="✅ Javobingiz saqlandi", reply_markup=back_to_menu)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await state.finish()


@dp.callback_query_handler(text="no", state=CreateQuestionnaireState.ish_muvozanati_va_farovonligi)
async def cancel_save_function(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer(text="❌ Saqlash bekor qilindi", reply_markup=back_to_menu)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await state.finish()


@dp.callback_query_handler(state=CreateQuestionnaireState.ish_muvozanati_va_farovonligi)
async def get_mark_for_ish_muvozanati_va_farovonligi(call: types.CallbackQuery, state: FSMContext):
    mark = call.data
    mark = int(mark)
    await state.update_data(ish_muvozanati_va_farovonligi=mark)
    data = await state.get_data()
    branch_id = data.get('branch_id')
    branch = await db.select_branch(branch_id=branch_id)
    rank_id = data.get('rank_id')
    rank = await db.select_rank(rank_id=rank_id)
    ish_muhiti_va_madaniyati = data.get('ish_muhiti_va_madaniyati')
    rivojlanish_va_osish_imkoniyatlari = data.get('rivojlanish_va_osish_imkoniyatlari')
    ish_haqi_va_mukofotlar = data.get('ish_haqi_va_mukofotlar')
    rahbariyat_bilan_munosabat = data.get('rahbariyat_bilan_munosabat')
    ish_muvozanati_va_farovonligi = data.get('ish_muvozanati_va_farovonligi')

    text = f"✅ Siz quyidagicha baholadingiz:\n" \
           f"📍 Filial: {branch['name']}\n" \
           f"🏢 Lavozim: {rank['name']}\n" \
           f"🌍 Ish muhiti va madaniyati: {ish_muhiti_va_madaniyati}\n" \
           f"📈 Rivojlanish va o'sish imkoniyatlari: {rivojlanish_va_osish_imkoniyatlari}\n" \
           f"💰 Ish haqi va mukofotlar: {ish_haqi_va_mukofotlar}\n" \
           f"👥 Rahbariyat bilan munosabatlar: {rahbariyat_bilan_munosabat}\n" \
           f"⚖️ Ish muvozanati va farovonlik: {ish_muvozanati_va_farovonligi}"
    await call.message.edit_text(text=text)
    await call.message.answer(text="Ushbu javobingizni saqlansinmi?", reply_markup=confirm_keyboard)
