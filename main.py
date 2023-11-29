import requests

from aiogram import Bot, Dispatcher,types,executor

TOKEN = "6608141145:AAHRM59PeN6XNdMt-wD51G62TxLr5EJAbKA"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer("Asalomu aleykum men botman")
    # await message.reply("Salom")
# @dp.message_handler()
# async def gf(message: types.Message):
#     await message.answer(message.text)
# import requests
url = " https://v6.exchangerate-api.com/v6/947cf3ded76cb7716f1f6de2/latest/USD"

response = requests.get(url)
data = response.json()
# kurs = data["conversion_rate"]
# print(kurs)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)