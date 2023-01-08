from telegram import Update
from telegram.ext import ContextTypes
from telegram import ForceReply, Update

import dreams.spankbang as sb
import dreams.ukevids as uk
import dreams.pornone as pn
from tools import send_video







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
    user = update.effective_user
    await update.message.reply_html(rf"A moment, {user.mention_html()}, the video's are in requisition! Please, wait!")
    videos = sb.search_porn(query,page_limit=10)
    await send_video(videos,update)
    # size = len(videos['videos'])
    # ping = videos['ping']
    # pages = videos['len_pages']
    # site_name = 'spankbang'
    # await update.message.reply_html(f'<b>We took {size} videos from {pages} pages from {site_name} in {ping:.2f} seconds.</b>')
    # await update.message.reply_html('<i>sennding videos ...</i>')
    # for i,video in enumerate(videos['videos']):
    #     #print(video)
    #     i = i+1
    #     title = video['title']
    #     time = video['time']
    #     url = video['url']
    #     stats = video['stats'].replace('\n',' ')
    #     query_tag = f' {query}'.replace(' ',' #')
    #     title_tag = f' {title}'.replace(' ',' #')
    #     caption = f'<b>[{i}/{size}]</b>\n\n<b>title:</b> {title}\n\n<b>time:</b> <i>{time}</i>\n\n<b>url:</b> {url}\n\n<b>stats: </b>{stats}\n\n<b>tags: </b>{query_tag} {title_tag} #{site_name}'
    #     try:
    #         await update.message.reply_animation(video['preview'],caption=caption,parse_mode=ParseMode.HTML)
    #     except:
    #         puts('[{i}] error spankbang: dont send image gif')
    #         #await update.message.reply_html(caption)
    #         try:
    #             await update.message.reply_photo(video['thumbnail'],caption=caption,parse_mode=ParseMode.HTML)
    #         except:
    #             puts(f'[{i}] error ukevids: dont send image png')
    #             await update.message.reply_html(caption)
    #             pass



async def ukevids(update:Update,context:ContextTypes.DEFAULT_TYPE) -> None:
    query = update.message.text.replace('/ukevids','')
    user = update.effective_user
    await update.message.reply_html(rf"A moment, {user.mention_html()}, the video's are in requisition! Please, wait!")
    videos = uk.search_porn(query,page_limit=10)
    await send_video(videos,update)
    # size = len(videos['videos'])
    # ping = videos['ping']
    # pages = videos['len_pages']
    # site_name = 'ukevids'
    # await update.message.reply_html(f'<b>We took {size} videos from {pages} pages from {site_name} in {ping:.2f} seconds.</b>')
    # await update.message.reply_html('<i>sennding videos ...</i>')
    # for i,video in enumerate(videos['videos']):
    #     #print(video)
    #     i = i+1
    #     title = video['title']
    #     time = video['time']
    #     url = video['url']
    #     stats = video['views']
    #     query_tag = f' {query}'.replace(' ',' #')
    #     title_tag = f' {title}'.replace(' ',' #')
    #     caption = f'<b>[{i}/{size}]</b>\n\n<b>title:</b> {title}\n\n<b>time:</b> <i>{time}</i>\n\n<b>url:</b> {url}\n\n<b>views: </b>{stats}\n\n<b>tags: </b>{query_tag} {title_tag} #{site_name}'
    #     # try:
    #     #     await update.message.reply_animation(video['gif'],caption=caption)
    #     # except:
    #     #     puts('[{i}] error spankbang: dont send image gif')
    #     try:
    #         await update.message.reply_photo(video['thumbnail'],caption=caption,parse_mode=ParseMode.HTML)
    #     except:
    #         puts(f'[{i}] error ukevids: dont send image png')
    #         await update.message.reply_html(caption)
    #         pass


async def pornone(update:Update,context:ContextTypes.DEFAULT_TYPE) -> None:
    #res_video = rq.get('https://s279.pornone.com/vid2/aQCDxuAHuggNdcE660d3EA/1672897195/23/278036723/278036723_480x320_400k.mp4')
    query = update.message.text.replace('/ukevids','')
    user = update.effective_user
    await update.message.reply_html(rf"A moment, {user.mention_html()}, the video's are in requisition! Please, wait!")
    videos = pn.search_porn(query,page_limit=10)
    await send_video(videos,update)
    # await update.message.reply_text('<b>test</b>\n<i>test</i>',parse_mode=ParseMode.HTML) #secure=SSbblZUnGD9b7ifN6tdXRw,1672939943&m=1&d=2&_tid=9262723')
