from telegram import Update
from telegram.constants import ParseMode
from kitano import puts



async def send_video(videos_data,update:Update):
    size = len(videos_data.videos)
    ping = videos_data.ping
    pages = videos_data.len_pages
    site_name = videos_data.site_name
    query = videos_data.query
    await update.message.reply_html(f'<b>We took {size} videos_data from {pages} pages from {site_name} in {ping:.2f} seconds.</b>')
    await update.message.reply_html('<i>sennding videos_data ...</i>')
    
    for i,video in enumerate(videos_data.videos):
        #print(video)
        i = i+1
        title = video.title #title = re.sub('[^A-Za-z0-9]+', '', title)
        time = video.time
        url = video.url
        stats_str = 'stats'
        try:
            stats = video.stats.replace('\n',' ')
        except:
            stats =video.views
            stats_str = 'views'
            pass
        query_tag = f' {query}'.replace('+',' #')
        title_tag = f' {title}'.replace(' ',' #')
        caption = f'<b>[{i}/{size}]</b>\n\n<b>title:</b> {title}\n\n<b>time:</b> <i>{time}</i>\n\n<b>url:</b> {url}\n\n<b>{stats_str}: </b>{stats}\n\n<b>tags: </b>{query_tag} {title_tag} #{site_name}'
        try:
            await update.message.reply_animation(video.preview,caption=caption,parse_mode=ParseMode.HTML)
        except:
            puts(f'[{i}] error spankbang: dont send image gif')
            #await update.message.reply_html(caption)
            try:
                await update.message.reply_photo(video.thumbnail,caption=caption,parse_mode=ParseMode.HTML)
            except:
                puts(f'[{i}] error ukevids: dont send image png')
                await update.message.reply_html(caption)
                pass