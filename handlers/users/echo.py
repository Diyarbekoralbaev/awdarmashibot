from aiogram import Bot, types
import requests
from loader import dp, bot

# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await bot.send_chat_action(message.chat.id, types.ChatActions.TYPING)
    url = 'https://api.diyarbek.uz/awdarma'
    data = {
    'text': message.text
     }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        result = response.json()
        await message.answer(result['awdarma'])
    else:
        pass