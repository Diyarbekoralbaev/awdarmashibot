from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, bot 


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await bot.send_chat_action(message.chat.id, types.ChatActions.TYPING)
    await message.answer(f"Salem, {message.from_user.full_name}!\n👋 Assalawma Aleykum bul bot jardeminde siz telegramnan shiqpagan halda barshe tilden Qaraqalpaq tiline tez ham sapali awdarma qilsaniz boladi\n✍️ Awdarma qiliw ushin magan tekstti jiberseniz boldi. Bot siz jibergen so'zdi qaysi tilde ekenligin aniqlap sizge Qaraqalpaq tiline awdarma qilip beredi\n\n🧑‍💻 Bul bot @Diyarbek_Dev tarepinen jaratilgan. \n📢 Kanalimiz: @Diyarbek_Blog")
