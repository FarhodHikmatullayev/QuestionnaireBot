from aiogram.dispatcher.filters.state import StatesGroup, State


class DownloadQuestionnairesState(StatesGroup):
    branch_id = State()