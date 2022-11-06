from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from telegram import ForceReply, Update
from os import getenv
import kitano as kt
from dotenv import load_dotenv
import logging


load_dotenv()

p = kt.Puts()
puts = p.puts

token = getenv('TELEGRAM_BOT_TOKEN')


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)




async def startt(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')






async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)





def main():
	app = Application.builder().token(token).build()

	app.add_handler(CommandHandler("start", start))
	app.add_handler(CommandHandler("help", help_command))


	app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
#	app.add_handler(CommandHandler("start", hello))
	puts('initializing app...')
	app.run_polling()



if __name__ =='__main__':
	main()
