from aiogram import Router, types, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from bot_config import database


complaint_router = Router()

class KofeComplaint(StatesGroup):
    name = State()
    phone = State()
    complaint = State()


@complaint_router.callback_query(F.data == "complaint")
async def feedback_start(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Имя?")
    await state.set_state(KofeComplaint.name)

@complaint_router.message(KofeComplaint.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Номер телефона?")
    await state.set_state(KofeComplaint.phone)

@complaint_router.message(KofeComplaint.phone)
async def process_phone(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("Жалоба?")
    await state.set_state(KofeComplaint.complaint)

@complaint_router.message(KofeComplaint.complaint)
async def process_complaint(message: types.Message, state: FSMContext):
    await state.update_data(complaint=message.text)
    await message.answer("Жалоба сохранено")
    data = await state.get_data()
    database.save_complaint(data)
    await state.clear()