# Please Add Your HTTP Access Token (api_key) on line below
api_key="YOUR_API_KEY"

base_url="https://saurav.tech/NewsAPI/top-headlines/category/"

#  Country code ( case sensitive )  in,us,au,ru,fr,gb
#  Cateogires business,entertainment,general,health,science,sports,technology




import requests
from telegram import *
from telegram.ext import *
import json
from sys import getsizeof


def truncate_string(value, max_length=4096, suffix=''):
    string_value = str(value)
    string_truncated = string_value[:min(len(string_value), (max_length - len(suffix)))]
    suffix = (suffix if len(string_value) > max_length else '')
    return string_truncated+suffix


def sort(requestCode):
    parts=requestCode.split("_")
    return getNews(parts[0],parts[1])
    
def getShortMsg(message):
    if getsizeof(message)<4096:
        return message
    elif getsizeof(message)>4096:
        return truncate_string(message)




def getNews(country,category):
    message=""
    ping_url=base_url+category+"/"+country+".json"
    response = requests.get(ping_url)
    news=json.loads(response.content)
    new_list=news['articles']
    for item in new_list:
        message+=item['title']
        message+="\n"
        message+=item['url']
        message+="\n"
    return getShortMsg(message)





def do_something(user_input):
    return sort(user_input)
    

def reply(update, context):
    user_input = update.message.text
    try:
        update.message.reply_text(do_something(user_input))
    except:
        update.message.reply_text("Something went wrong! Can you please rephrase")


def main():
    updater = Updater(api_key, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, reply))
    updater.start_polling()
    updater.idle()

main()