import logging
import wikipedia
from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = ('6196789147:AAFmpSTPRnZIfBbzSwhAphAqB4iVHZrnuv4')
wikipedia.set_lang('uz')
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
db = Dispatcher(bot)
@db.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(f'<b><em>Assalomu alaykum! {message.from_user.full_name}</em></b>\n \nBizning  "Ma\'lumotlar" izlovchi🔎  botimizga🤖  hush kelibsiz\n \n Kerakli ma\'lumotni topish uchun istalgan so\'zni kiriting!', parse_mode='HTML')
@db.message_handler()
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
         await message.answer('Ushbu buyruq noto\'g\'ri kiritildi🚫 yoki maqola mavjud emas❌')
@db.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.answer(f'<b><em>Assalomu alaykum! {message.from_user.full_name}</em></b>\n \nBizning  "Ma\'lumotlar" izlovchi🔎  botimizga🤖  hush kelibsiz\n \n Kerakli ma\'lumotni topish uchun istalgan so\'zni kiriting!', parse_mode='HTML')
if __name__ == '__main__':
    executor.start_polling(db, skip_updates=True)
