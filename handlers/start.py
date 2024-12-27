from aiogram.filters import Command
from aiogram import Router, types

start_router = Router()



@start_router.message(Command('start'))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=
        [
            [
                types.InlineKeyboardButton(text="Оставить жалобу", callback_data='complaint')
            ]
        ]
    )
    await message.answer(f"Привет {name}.", reply_markup=kb)