import logging

from aiogram import Dispatcher, Bot, executor
from aiogram.types import *
from keyboard import start_btn, language_btn, choice_city_btn, karakalpakstan_btn, tashkent_city_btn, tashkent_btn


logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "6133862492:AAFn8bLnEQaLlGPK3ZPBNNyDZsPGHpMfEdg"

bot = Bot(token=BOT_TOKEN, parse_mode='html')
dp = Dispatcher(bot=bot)



@dp.message_handler(commands=['start'])
async def start_handler(message: Message):
    btn = await start_btn()
    await message.answer("💊 Введите название лекарства", reply_markup=btn)


@dp.message_handler()
async def text_handler(message: Message):
    countries = ['', 'Република Каракалпакстан', 'Ташкент', 'Ташкентская область', 'Андижан', 'Бухара', 'Самарканд',
                 'Джизак','Кашкадарья', 'Навои', 'Наманган', 'Сурхандарья', 'Сырдарья', 'Фергана', 'Хорезм']
    
    text = message.text
    if text == "🔍 Начать поиск":
        await message.answer("💊 Отправьте название лекарства (не менее 3 букв)")

    elif text == "✍️ Оставить отзыв":
        await message.answer("Уважаемый пользователь, через этот бот Вы можете направить свои мнения и предложения. @osonaptekamurojatbot.")

    elif text == "🔄 Изменить язык":
        btn = await language_btn()
        await message.answer("Выберите язык 👇", reply_markup=btn)

    elif text == "📍 Мое местоположение":
        btn = await choice_city_btn()
        await message.answer("Выберите город", reply_markup=btn)

    elif text == "Как пользоваться❓":
        await message.answer_video(InputFile("1.mp4"))

    elif text == "⏪ Назад":
        btn = await start_btn()
        await message.answer("💊 Введите название лекарства", reply_markup=btn)

    elif text == "По Всему Узбекистану":
        btn = await start_btn()
        await message.answer("💊 Введите название лекарства", reply_markup=btn)

    elif text == "Реcпублика Каракалпакстан":
        btn = await karakalpakstan_btn()
        await message.answer("Выберите местность", reply_markup=btn)

    elif text == "Ташкент":
        btn = await tashkent_city_btn()
        await message.answer("Выберите местность", reply_markup=btn)

    elif text == "Ташкентская область":
        btn = await tashkent_btn()
        await message.answer("Выберите местность", reply_markup=btn)




if __name__ == "__main__":
    executor.start_polling(dp)
