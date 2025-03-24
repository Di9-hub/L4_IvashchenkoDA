from aiogram import Bot, Dispatcher, types,Router,filters, F
import asyncio
from config import API_TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

start_router = Router()

@start_router.message(filters.CommandStart())
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот, который повторяет за тобой.")

@start_router.message(filters.Command("help"))
async def command_help_handler(message: types.Message)-> None:
    help_text = """
        Доступные команды:
        /start - Начать диалог с ботом
        /help - Получить список доступных команд
        (Все остальные сообщения) - Бот повторяет ваше сообщения
        """
    await message.answer(help_text)


@start_router.message(F.text)
async def echo(message: types.Message):
    user_message = message.text
    await message.answer(f"Вы сказали: {user_message}")

async def main():
    dp.include_router(start_router)
    await bot.delete_webhook(drop_pending_updates = True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())