#Я многие вещи не понял, поэтому посмотрел уроки на ютубе
#Из-за этого способ написания чуть отличается от того, какой был на уроке.
#Tокен - 6445594361:AAG0EOKUMBL-uvldN1OA8jxGGjEkyODnO3Q

import asyncio
import dotenv
from aiogram import Bot, executor, Dispatcher, types
from dotenv import load_dotenv
from random import choice
from os import getenv
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton


load_dotenv()
IMAGES = ['https://www.google.com/imgres?imgurl=https%3A%2F%2Fih1.redbubble.net%2Fimage.2415420317.7991%2Fflat%2C750x%2C075%2Cf-pad%2C750x1000%2Cf8f8f8.jpg&tbnid=jwR6otbA4cPDpM&vet=12ahUKEwib4evb6oKDAxU_JRAIHRETBOAQMygEegQIARBY..i&imgrefurl=https%3A%2F%2Fwww.redbubble.com%2Fi%2Fart-board-print%2FFunny-Dog-Face-by-martimmendes%2F79627991.NVL2T&docid=om6DnufkkmlVfM&w=750&h=1000&q=funny%20dog&ved=2ahUKEwib4evb6oKDAxU_JRAIHRETBOAQMygEegQIARBY',
          'https://www.google.com/imgres?imgurl=https%3A%2F%2Fi.insider.com%2F5d124f9a9c5101048e440825%3Fwidth%3D1000%26format%3Djpeg%26auto%3Dwebp&tbnid=S82u0yle1kcbBM&vet=12ahUKEwib4evb6oKDAxU_JRAIHRETBOAQMygAegQIARBO..i&imgrefurl=https%3A%2F%2Fwww.insider.com%2Ffunny-dog-pictures-perfect-timing-2019-6&docid=gs0oed2EcxIFIM&w=971&h=728&q=funny%20dog&ved=2ahUKEwib4evb6oKDAxU_JRAIHRETBOAQMygAegQIARBO'
          'https://www.google.com/imgres?imgurl=https%3A%2F%2Fmedia.tenor.com%2FeDBZxaIJl04AAAAM%2Ffgty.gif&tbnid=3sszWO_jZXBmAM&vet=12ahUKEwib4evb6oKDAxU_JRAIHRETBOAQMygUegQIARB9..i&imgrefurl=https%3A%2F%2Ftenor.com%2Fsearch%2Ffunny-dog-gifs&docid=yPeeV9qABIuJqM&w=220&h=275&q=funny%20dog&ved=2ahUKEwib4evb6oKDAxU_JRAIHRETBOAQMygUegQIARB9'
          'https://www.google.com/imgres?imgurl=https%3A%2F%2Fpetapixel.com%2Fassets%2Fuploads%2F2015%2F12%2Fdogs-catching-treats-by-christian-vieler-6-600x800.jpg&tbnid=2vFbto0nPVowOM&vet=12ahUKEwib4evb6oKDAxU_JRAIHRETBOAQMygeegUIARCaAQ..i&imgrefurl=https%3A%2F%2Fpetapixel.com%2F2022%2F01%2F11%2Fhumorous-photos-of-dogs-catching-flying-treats%2F&docid=MMG3OqmITB9jbM&w=600&h=800&q=funny%20dog&ved=2ahUKEwib4evb6oKDAxU_JRAIHRETBOAQMygeegUIARCaAQ'
          'https://www.google.com/imgres?imgurl=https%3A%2F%2Fimages.unsplash.com%2Fphoto-1518020382113-a7e8fc38eac9%3Fq%3D80%26w%3D1000%26auto%3Dformat%26fit%3Dcrop%26ixlib%3Drb-4.0.3%26ixid%3DM3wxMjA3fDB8MHxzZWFyY2h8M3x8ZnVubnklMjBkb2d8ZW58MHx8MHx8fDA%253D&tbnid=HX9RyPVtiUQxnM&vet=12ahUKEwib4evb6oKDAxU_JRAIHRETBOAQMygqegUIARC0AQ..i&imgrefurl=https%3A%2F%2Funsplash.com%2Fs%2Fphotos%2Ffunny-dog&docid=waAN9OHjiWWl0M&w=1000&h=1393&q=funny%20dog&ved=2ahUKEwib4evb6oKDAxU_JRAIHRETBOAQMygqegUIARC0AQ']

bot = Bot(getenv('BOT_TOKEN'))
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup()
b1 = KeyboardButton('/start')
b2 = KeyboardButton('/myinfo')
b3 = KeyboardButton('/random_pic')
kb.add(b1).add(b2).add(b3)

@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    await msg.answer(text=f'Hello, {msg.from_user.first_name}!', reply_markup=kb)
    await msg.delete()

@dp.message_handler(commands=['myinfo'])
async def info(msg: types.Message):
    await msg.answer(text=f'''
    Your's info:
    id: {msg.from_user.id}
    first_name: {msg.from_user.first_name}
    surname: {msg.from_user.username}''')

@dp.message_handler(commands=['random_pic'])
async def rndm_pc(msg: types.Message):
    await msg.answer_photo(photo=f'{choice(IMAGES)}', caption='Random picture from catalog:')

async def main():
    await bot.set_my_commands([
        types.BotCommand(command='start',description='Getting started to work'),
        types.BotCommand(command='myinfo',description='Get your info'),
        types.BotCommand(command='random.pic',description='get rahdom picture')
    ])
    await dp.start_polling(bot)
#Вот тут у меня почему-то не создавалoсь меню, поэтому я создал клавиатуру



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    asyncio.run(main())
