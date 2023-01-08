from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from telegram import ForceReply, Update
from telegram.constants import ParseMode
from os import getenv
from dotenv import load_dotenv
import logging
import requests as rq
from kitano import puts
import dreams.spankbang as sb
import dreams.ukevids as uk

from commands import start,help_command,spankbang,ukevids,pornone,echo





load_dotenv()
token = getenv('TOKEN_TELEGRAM_BOT')
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)






def main():
    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("spankbang", spankbang))
    app.add_handler(CommandHandler('ukevids',ukevids))
    app.add_handler(CommandHandler('pornone',pornone))


    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
#	app.add_handler(CommandHandler("start", hello))
    puts('initializing app...')
    app.run_polling()



if __name__ =='__main__':
	main()
