# Please Add Your HTTP Access Token (api_key) on line below
api_key="YOUR_API_KEY"
base_url="https://bank-apis.justinclicks.com/API/V1/IFSC/"

#  Country code ( case sensitive )  in,us,au,ru,fr,gb
#  Cateogires business,entertainment,general,health,science,sports,technology




import requests
from telegram import *
from telegram.ext import *
import json
from sys import getsizeof


def truncate_string(value, max_length=4096, suffix=''): 
    string_value = str(value)
    string_truncated = string_value[: min(len(string_value), (max_length - len(suffix)))]
    suffix = (suffix if len(string_value) > max_length else '')
    return string_truncated+suffix


def sort(IFSC): 
    return getData(IFSC)
    
def getShortMsg(message): 
    if getsizeof(message)<4096: 
        return message
    elif getsizeof(message)>4096: 
        return truncate_string(message)
def emptyd(strd): 
    if strd=="" or strd==None: 
        return 'Not Found'
    else: 
        return strd

def getBoool(bool): 
    if bool: 
        return 'Yes'
    else: 
        return 'False'

def getData(IFSC): 
    ping_url=base_url+IFSC.upper()+"/"
    response = requests.get(ping_url)
    data=json.loads(response.content)
    Message="We found details below for given IFSC Code\n"
    Message+="Bank Name : "+data["BANK"]
    Message+="\nBank Code : "+data["BANKCODE"]
    Message+="\nBranch Name : "+data["BRANCH"]
    Message+="\nCenter : "+data["CENTRE"]
    Message+="\nCity : "+data["CITY"]
    Message+="\nContact : "+str(data["CONTACT"])
    Message+="\nDistrict : "+data["DISTRICT"]
    Message+="\nIFSC : "+getBoool( data["IFSC"])
    Message+="\nIMPS : "+getBoool(data["IMPS"])
    Message+="\nMICR : "+str(data["MICR"])
    Message+="\nNEFT : "+getBoool(data["NEFT"])
    Message+="\nRTGS : "+getBoool(data["RTGS"])
    Message+="\nSTATE : "+data["STATE"]
    Message+="\nSWIFT : "+emptyd(data["SWIFT"])
    Message+="\nUPI : "+getBoool(data["UPI"])
    Message+="\nAddress : "+data["ADDRESS"]

    return getShortMsg(Message)





def do_something(user_input): 
    return sort(user_input)
    

def reply(update, context): 
    user_input = update.message.text
    try: 
        update.message.reply_text(do_something(user_input))
    except: 
        update.message.reply_text("Something went wrong! Can you please re-enter")


def main(): 
    updater = Updater(api_key, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, reply))
    updater.start_polling()
    updater.idle()

main()