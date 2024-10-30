from aiogram.dispatcher.filters.state import StatesGroup, State


class CreateQuestionnaireState(StatesGroup):
    user_id = State()
    branch_id = State()
    rank_id = State()
    ish_muhiti_va_madaniyati = State()
    rivojlanish_va_osish_imkoniyatlari = State()
    ish_haqi_va_mukofotlar = State()
    rahbariyat_bilan_munosabat = State()
    ish_muvozanati_va_farovonligi = State()