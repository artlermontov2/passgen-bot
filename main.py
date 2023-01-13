import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
import generator as gen

load_dotenv()

# Токен бота
API_TOKEN = os.getenv('BOT_TOKEN')

# Настройка ведения журнала логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера.
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def start_func(message: types.Message):
    await_text = (
        f'👋Привет, я бот для генерации пароля!\n\n'
        f'✳По умолчанию:\n'
        f'Пароль содержит латинские буквы в нижнем регистре и имеет длину 8 символов 👉 /pass\n\n'
        f'✅Есть несколько параметров, которые можно менять:\n'
        f'✅up -  добавит буквы в верхнем регистре.\n'
        f'✅num - добавит цифры.\n'
        f'✅spec - добавит спец. символы.\n'
        f'✅так же можно изменить длинну пароля, добавив к примеру: 12.\n\n'
        f'✴Пример ввода:\n'
        f'✴"up num 12" - это значит,\n'
        f'что пароль будет содержать сиволы в нижнем и верхнем регистре,\n'
        f'цифры, и длинна его будт равна 12 символам.\n\n'
        f'‼Важно: между вводом доп. параметров должен '
        f'стоять пробел, иначе эти параметры не будут учтены.'
    )
    await message.answer(await_text)


@dp.message_handler(commands=['pass'])
async def defualt_pass(message: types.Message):
    await message.answer(gen.password(gen.pars_msg('')))


@dp.message_handler()
async def gen_pass(message: types.Message):
    msg = gen.pars_msg(message.text)
    await message.answer(gen.password(msg))

    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)