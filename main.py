import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from config import BOT_TOKEN, ADMIN_ID
from handlers import router
from utils import setup_db
from emoji_config import AnimatedEmoji

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

async def on_startup():
    await setup_db()
    await bot.send_message(
        chat_id=ADMIN_ID,
        text=f"<tg-emoji emoji-id='{AnimatedEmoji.HEART}'>🤖</tg-emoji> "
             "<b>Бот успешно запущен!</b>",
        parse_mode="HTML"
    )

async def main():
    await on_startup()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())