import asyncio
from bot_config import bot, dp, database
from handlers.start import start_router
from handlers.complaint_dialog import complaint_router


async def on_startup(bot):
    database.create_tables()

async def main():
    dp.include_router(start_router)
    dp.include_router(complaint_router)
    dp.startup.register(on_startup)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

