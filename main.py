from config import dp
from aiogram.utils import executor
from handlers import callback, client, admin, extra, fsmAdminMentor, fsm_anketa
import logging

fsmAdminMentor.register_handlers_mentor(dp)
fsm_anketa.register_handlers_anketa(dp)
client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)

extra.register_handlers_extra(dp)



if  __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp,  skip_updates=True)