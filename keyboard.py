from aiogram.types import *


async def start_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn.row('🔍 Начать поиск')
    btn.add(
        KeyboardButton('✍️ Оставить отзыв'),
        KeyboardButton('🔄 Изменить язык'),
    )
    btn.row('📍 Мое местоположение')
    btn.row('Как пользоваться❓')

    return btn


async def language_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn.add(
        KeyboardButton('🇺🇿 UZ'),
        KeyboardButton('🇷🇺 RU'),
        KeyboardButton('🇺🇸 EN'),
        KeyboardButton('⏪ Назад'),
    )

    return btn


async def choice_city_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn.add(
        KeyboardButton('По Всему Узбекистану'),
        KeyboardButton('Реcпублика Каракалпакстан'),
        KeyboardButton('Ташкент'),
        KeyboardButton('Ташкентская область'),
        KeyboardButton('Андижан'),
        KeyboardButton('Бухара'),
        KeyboardButton('Самарканд'),
        KeyboardButton('Джизак'),
        KeyboardButton('Кашкадарья'),
        KeyboardButton('Навои'),
        KeyboardButton('Наманган'),
        KeyboardButton('Сурхандарья'),
        KeyboardButton('Сырдарья'),
        KeyboardButton('Фергана'),
        KeyboardButton('Хорезм'),
        KeyboardButton('⏪ Назад'),
    )

    return btn


async def karakalpakstan_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn.row('Вся Республика Каракалпакстан')
    btn.add(
        KeyboardButton('Беруний'),
        KeyboardButton('г.Нукус'),
        KeyboardButton('Караузяк'),
        KeyboardButton('Ходжейли'),
    )
    btn.row('⏪ Назад')

    return btn


async def tashkent_city_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn.row('Весь Ташкент')
    btn.add(
        KeyboardButton('Бектемир'),
        KeyboardButton('Чиланзар'),
        KeyboardButton('Мирабад'),
        KeyboardButton('Мирзо-Улугбек'),
        KeyboardButton('Алмазар'),
        KeyboardButton('Шайхонтохур'),
        KeyboardButton('Сергели'),
        KeyboardButton('Учтепа'),
        KeyboardButton('Яккасарай'),
        KeyboardButton('Яшнабад'),
        KeyboardButton('Юнусабад'),
        KeyboardButton('Янгихаёт'),
    )
    btn.row('⏪ Назад')

    return btn


async def tashkent_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn.row('Вся Ташкентская Область')
    btn.add(
        KeyboardButton('Ангрен'),
        KeyboardButton('г.Бекабад'),
        KeyboardButton('Бекабадский район'),
        KeyboardButton('Бука'),
        KeyboardButton('Бостанлык'),
        KeyboardButton('Чиназ'),
        KeyboardButton('Чирчик'),
        KeyboardButton('Нурафшан'),
        KeyboardButton('Ахангаран'),
        KeyboardButton('Алмалык'),
        KeyboardButton('Аккурган'),
        KeyboardButton('Уртачирчик'),
        KeyboardButton('Паркент'),
        KeyboardButton('Пскент'),
        KeyboardButton('Кибрай'),
        KeyboardButton('Ташкентский район'),
        KeyboardButton('г.Янгиюль'),
        KeyboardButton('Янгиюлький район'),
        KeyboardButton('Юкоричирчик'),
        KeyboardButton('Зангиота'),
    )
    btn.row('Куйичирчик')
    btn.row('⏪ Назад')

    return btn