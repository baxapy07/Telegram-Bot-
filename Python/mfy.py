from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
button1 = InlineKeyboardButton(text='👮‍MFY Hodimlari', callback_data='mfy', resize_keyboard=True)
button2 = InlineKeyboardButton(text='👩‍🏫Maktablar', callback_data='maktab')
button3 = InlineKeyboardButton(text='👩‍⚕️MTM hodimlari', callback_data='bohcha')
button4 = InlineKeyboardButton(text='👩‍⚕️QOP SHifokorlari', callback_data='duxtr')
button5 = InlineKeyboardButton(text='🧑‍🍳Oshxonalar', callback_data='osh')
button6 = InlineKeyboardButton(text='☪️Masjid imomi-hatibi', callback_data='masjid')
button7 = InlineKeyboardButton(text='🏦Do\'konlar', callback_data='dokon')
button8 = InlineKeyboardButton(text='👨‍🔧Ustaxonalar', callback_data='usta')
button9 = InlineKeyboardButton(text='🛣Ko\'chalar', callback_data='kocha')

keyboard_inline = InlineKeyboardMarkup().add(button1, button2).add(button3).add(button4, button5).add(button6).add(button7,button8).add(button9)
bot = Bot(token='6081797106:AAHdajFQwuciSklHiMpBhc5ayHp4_xZmteE')
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def random_answer(message: types.Message):
     await message.reply(f"<b>Assalomu alaykum! <em>{message.from_user.full_name}</em></b>\n \nQizil To'qay Mahalla Fuqarolar yig'ini haqida ma'lumotlar botiga hush kelibsiz!", parse_mode='HTML')
     await message.reply('Ma\'lumot olish uchun quyidagilardan birini tanlang👇', reply_markup=keyboard_inline)
@dp.callback_query_handler(text=['mfy', 'maktab', 'bohcha', 'duxtr', 'osh', 'masjid', 'dokon', 'usta', 'kocha'])
async def random_value(call: types.CallbackQuery):
    if call.data == 'mfy':
       await call.message.answer('Ma\'lumotlar:\n\nMahalla Raisi: Ruziyev.D\n☎️ +998970601231\n\nHokim yordamchisi: Abubakirov.B\n☎ +998973399577\n\nYoslar yetakchisi: Baxtiyorjon\n☎️ +998993213799\n\nHotin qizlar faoli: O\'rinboyeva.H\n☎️ +998770014210')
    if call.data == 'maktab':
       await call.message.answer('Hozircha ma\'lumot mavjud emas🤷')
    if call.data == 'bohcha':
       await call.message.answer('Hozircha ma\'lumot mavjud emas🤷')
    if call.data == 'duxtr':
       await call.message.answer('Ma\'lumotlar:\n\nShifokor:Lobarxon\n☎️ +998999547466')
    if call.data == 'osh':
       await call.message.answer('Hozircha ma\'lumot mavjud emas🤷')
    if call.data == 'masjid':
       await call.message.answer('M\'lumotlar:\n\nMasjid kotibi: To\'lqinjon\n☎️ +998934405209\n\nMasjid mutavalisi: Olimjon\n☎ +998993961856\n\nQurilish ma\'suli: Ilhomjon\n☎ +998929370189')
    if call.data == 'dokon':
       await call.message.answer('Ma\'lumotlar\n\nDo\'kon rahbari: I.Oybek\n☎ +998909370189')
    if call.data == 'usta':
       await call.message.answer('Hozircha ma\'lumot mavjud emas🤷')
    if call.data == 'kocha':
        
       await call.message.answer('Ma\'lumotlar:\n\n1-ko\'cha: Uch Qo\'rg\'on\n2-ko\'cha: Uychi\n3-ko\'cha: Qo\'rg\'oncha')
    await call.answer()
executor.start_polling(dp)
