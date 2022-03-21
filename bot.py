from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from my_bot.init_bot import dp
from my_bot.hendlers import send_welcome


async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()

if __name__ == '__main__':
    executor.start_polling(dp, on_shutdown=shutdown)
