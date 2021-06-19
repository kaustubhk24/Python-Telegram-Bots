# Python Telegram Bots

## Examples of bot developed
 First open the folder of bot you want to deploy and then open `tele-bot.py`  on 2nd line of this file just change value of `api_key` with your `API KEY [HTTP Access Token]`, Now you can deploy bot directly No other changes required



## Bots
* [IFSC Finder Telebot](https://github.com/kaustubhk24/Python-Telegram-Bots/#ifsc-finder-telebot)
* [News Telebot](https://github.com/kaustubhk24/Python-Telegram-Bots/#news-telebot)
* [Meme Bot](https://github.com/kaustubhk24/Python-Telegram-Bots/#meme-bot)
* [Image Search](https://github.com/kaustubhk24/Python-Telegram-Bots/#image-search)

## How to use?

### IFSC Finder Telebot
To use IFSC Finder just send any IFSC Code as message to bot, In reply it will send you all the available information for the given IFSC Code.
example `MAHB0001012`
### News Telebot
Get filtered news with Given Filters like country,category
example input  `in_business` this will send you all indian business news to you.

#### Countries Available
```
in
us
au
ru
fr
gb
```
##### Categories
```
business
entertainment
general
health
science
sports
technology

```
### Meme Bot
Meme bot is only contain one file that saves all the messages sent to it and take any message randomly and sends to user in return that's it.
To train this we need ```train- Traning Phrase ```
### Image Search
Image search Downloads number of images from Bing, Just Send input as ```Query_number of images```
Example ```Hummingbird_10``` This will send in return 10 images from bing search engine for Hummingbird

## Thanks to

* [Python Telegram Bot](https://github.com/python-telegram-bot/python-telegram-bot) : Used for basic functionality of Bot in all bots
* [NEWS API](https://github.com/SauravKanchan/NewsAPI) : Used for Fetching news
* [IFSC API](https://github.com/kaustubhk24/Indian-Banks-Data) : Used for Fetching Details by using IFSC
* [bing_image_downloader](https://github.com/gurugaurav/bing_image_downloader) : Used for downloading images from bing with Query
