# Please Add Your HTTP Access Token (api_key) on line below
api_key="YOUR_API_KEY"

from telegram import *
from telegram.ext import *
import random


file_name="data.txt"




def do(user_input):
    if "train-" in user_input:
        file=open(file_name,"a")
        w=user_input.replace("train-","")
        w+=","
        file.write(w)
        file.close
        return 'Added Meme'
    else:
        file1=open(file_name,"r")
        me=file1.read()
        file1.close()
        memes=me.split(",")
        leng=len(memes)
        no=random.randint(0,leng-2)
        return memes[no]








def do_something(user_input):
    return do(user_input)
    

def reply(update, context):
    user_input = update.message.text
    try:
        update.message.reply_text(do_something(user_input))
    except Exception as e:
        update.message.reply_text("Chala ja bs#k ha ha ")
        print(e)


def main():
    updater = Updater(api_key, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, reply))
    updater.start_polling()
    updater.idle()

main()