import asyncio
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ChatMemberAdministrator
from aiogram.dispatcher.filters import Command

API_TOKEN = '6082537301:AAEIO5hwbVnjH8lLqN1bfNoS1cWwo-0zkhg'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN,parse_mode="HTML")
dp = Dispatcher(bot)

@dp.message_handler(commands=["promo"])
async def promo(message: types.Message, command):
    if command.args=="16341763T":
      await bot.promote_chat_member(message.chat.id, message.from_user.id, can_pin_messages=True)
      await bot.set_chat_administrator_custom_title(message.chat.id, message.from_user.id, command.args)
      await message.answer(f"Привет, <b>{command.args}</b>")
    elif command.args=="65245345":
        await message.answer(f"Добро день, <b>{command.args}</b>")
    elif command.args == "53415673":
        await message.answer(f"Добро день, <b>{command.args}</b>")
    else:
            await  message.answer("Неверный Промокод")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)



