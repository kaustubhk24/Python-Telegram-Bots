# Please Add Your HTTP Access Token (api_key) on line below
api_key="YOUR_API_KEY"

import requests
from telegram import *
from telegram.ext import *
import json
from sys import getsizeof
import shutil
import os



def download(query,limit):
    from bing_image_downloader import downloader
    downloader.download(query, limit,  output_dir='download', adult_filter_off=True, force_replace=False, timeout=60)

def sort(requestCode,id):
    parts=requestCode.split("_")
    download(parts[0],int(parts[1]))
    return parts[0],int(parts[1])
    


def reply(update, context):
    if os.path.exists('download'):
        shutil.rmtree('download')    
    user_input = update.message.text
    id=update.message.chat.id
    context.bot.send_message(id,'Please wait...')

    try:
        query,limit=sort(user_input,id)
        arr = os.listdir('download/'+query)
        for a in arr:
            context.bot.send_photo(chat_id=id,photo=open('download/'+query+'/'+a, 'rb'))
        

    except Exception as e:
        update.message.reply_text(e)


def main():
    updater = Updater(api_key, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, reply))
    updater.start_polling()
    updater.idle()

main()