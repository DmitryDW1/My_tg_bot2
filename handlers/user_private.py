from aiogram import F, types, Router
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command, or_f
from aiogram.utils.formatting import (
    as_list,
    as_marked_section,
    Bold,
)  # Italic, as_numbered_list и тд

from filters.chat_types import ChatTypeFilter
from kbds import reply

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))

@user_private_router.message(CommandStart())
async def start(message: types.Message):
    await message.answer(
        'Привет, я первый бот, созданный DmitryDW1',
        reply_markup=reply.get_keyboard(
            "Меню",
            "Помощь",
            "О нас",
            "Варианты оплаты",
            "Варианты доставки",
            "Отправить номер телефона",
            placeholder='Что вы выбираете?',
            sizes=(3, 2)
        ),
    )

# @user_private_router.message(F.text.lower() == 'меню')
@user_private_router.message(or_f(Command('menu'), (F.text.lower() == 'меню')))
async def echo(message: types.Message):
    await message.answer('Посмотреть меню:')

@user_private_router.message(F.text.lower() == 'помощь')
@user_private_router.message(Command('help'))
async def echo(message: types.Message):
    await message.answer('Помощь:')

@user_private_router.message(F.text.lower() == 'о нас')
@user_private_router.message(Command('about'))
async def echo(message: types.Message):
    await message.answer('О нас:')

@user_private_router.message((F.text.lower().contains('плат')) | (F.text.lower() == 'варианты оплаты'))
@user_private_router.message(Command('payment'))
async def echco(message: types.Message):
    
    text = as_marked_section(
        Bold('Варианты оплаты:'),
        'Картой в боте',
        'При получении карта/кеш',
        'В заведении',
        marker='✅ '
        )
    
    await message.answer(text.as_html())

@user_private_router.message((F.text.lower().contains('достав')) | (F.text.lower() == 'варианты доставки'))
@user_private_router.message(Command('shipping'))
async def echo(message: types.Message):
    text = as_list(
        as_marked_section
        (
            Bold('Варианты доставки/заказа:'),
            'Курьер',
            'Самовынос (сейчас прибегу заберу)',
            'Поем у Вас (сейчас прибегу)',
            marker='✅ '
        ),
        as_marked_section
        (
            Bold('Нельзя:'),
            'Почта',
            'Голуби',
            marker='❌ '
        ),
        sep='\n-----------------------------\n'
    )
    await message.answer(text.as_html())

# @user_private_router.message((F.text.lower().contains('доставк')) | (F.text.lower() == 'варианты доставки'))
# async def echo(message: types.Message):
#     await message.answer('Это магический фильтр!')

# @user_private_router.message(F.text, F.text.lower() == 'варианты доставки')
# async def echo(message: types.Message):
#     await message.answer('Это магический фильтр!')

# @user_private_router.message(F.text)
# async def echo(message: types.Message):
#     await message.answer('Моя твоя не понимай...')

@user_private_router.message(F.photo)
async def echo(message: types.Message):
    await message.answer('О, фоточка)))')

@user_private_router.message(F.sticker)
async def echo(message: types.Message):
    await message.answer('Это стикер:)')


@user_private_router.message(F.contact)
async def get_contact(message: types.Message):
    await message.answer(f'Контакт')
    await message.answer(str(message.contact))

@user_private_router.message(F.location)
async def get_location(message: types.Message):
    await message.answer(f'Локация')
    await message.answer(str(message.location))