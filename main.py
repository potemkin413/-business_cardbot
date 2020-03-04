import aiogram
from aiogram import Bot, Dispatcher, executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token='1058450665:AAF1ssuVgkTP5RhrDDF90i6bcTqi9DWocW8')
dp = Dispatcher(bot)

about_me = InlineKeyboardButton('Обо мне✌🏻', callback_data='button5')
soc = InlineKeyboardButton('Я в соц.сетях👦🏼', url='https://vk.com/potemkin413')
couch = InlineKeyboardButton('Коуч группа👨🏼‍💻', url='https://vk.com/potemkin413')
history = InlineKeyboardButton('Поинтересоваться историей организации🕋', callback_data='button2')
contact_button= InlineKeyboardButton('Контактные данные📒', callback_data='button1')
contact_buttonkb = InlineKeyboardMarkup().add(about_me,soc).add(contact_button,couch).add(history)


@dp.callback_query_handler()
async def call_back_button1(callback_query):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 1:
        await bot.send_message(chat_id=callback_query.from_user.id,  text='📞 8-800-555-35-35\n✈ @Nikitochka413\n 📇 potemkin413@gmail.com')
    elif code ==2:
        await bot.send_message(chat_id=callback_query.from_user.id, text='Telegra - кроссплатформенный мессенджер, позволяющий обмениваться сообщениями и медиафайлами многих форматов. Используются проприетарная серверная часть c закрытым кодом, работающая на мощностях нескольких компаний США и Германии, финансируемых Павлом Дуровым в объёме порядка 13 млн долларов США ежегодно')
    elif code ==5:
        await bot.send_message(chat_id=callback_query.from_user.id, text='Python june developer, had start in 2019')


@dp.message_handler(commands=['start'])
async def welcome_message(message):
    await bot.send_message(chat_id=message.from_user.id, text="Привет👋🏻\nЯ первая версия 'Бота-визитки'\nНе ругайся, если я буду работать не правильно😉 \nЕсли ты хочешь узнать более подробную информацию или использовать какие-то мои возможности, выбирай соответсующую кнопку🤨", reply_markup=contact_buttonkb)

if __name__ == '__main__':
    executor.start_polling(dp)