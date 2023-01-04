from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from telegram import ForceReply, Update
from os import getenv
from dotenv import load_dotenv
import logging

from kitano import puts
import dreams.spankbang as sb

load_dotenv()

token = getenv('TOKEN_TELEGRAM_BOT')


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


async def spankbang(update:Update,context:ContextTypes.DEFAULT_TYPE) -> None:
    query = update.message.text.replace('/spankbang','')
    videos = sb.search_porn(query,page_limit=4)
    size = len(videos['videos'])
    for i,video in enumerate(videos['videos']):
        #print(video)
        i = i+1
        title = video['title']
        time = video['time']
        url = video['url']
        stats = video['stats'].replace('\n',' | ')
        caption = f'[{i}/{size}]\ntitle: {title}\ntime: {time}\nurl: {url}\nstats{stats}'
        try:
            await update.message.reply_animation(video['gif'],caption=caption)
        except:
            puts('[{i}] error spankbang: dont send image gif')
            try:
                await update.message.reply_photo(video['utl_img'],caption=caption)
            except:
                puts(f'[{i}] error spankbang: dont send image png')
                pass

def main():
    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("spankbang", spankbang))


    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
#	app.add_handler(CommandHandler("start", hello))
    puts('initializing app...')
    app.run_polling()



if __name__ =='__main__':
	main()
