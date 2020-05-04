import requests
from bs4 import BeautifulSoup
import time
'''
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CallbackContext
from telebot import apihelper
from telegram.ext import MessageHandler
from telegram.ext import Filters
'''


URL = 'https://ria.ru/economy/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}



#def


def get_last_name(html):
    soup = BeautifulSoup(html, 'html.parser')
    name = soup.find('a', class_ = 'list-item__title color-font-hover-only').get_text()
    return name

def get_html(url, params=None):
    r = requests.get(url, headers = HEADERS,params = params)
    return r

def get_link(html):
    global last_name 
    global URL
    soup = BeautifulSoup(html, 'html.parser')
    name = soup.find('a', class_ = 'list-item__title color-font-hover-only').get_text()
    link = soup.find('a', class_ = 'list-item__title color-font-hover-only').get('href')
    time_post = soup.find('div',class_ = 'list-item__date').get_text(),
    html = get_html(link)
    if last_name != name:
        last_name = name
        print(time_post)
        get_news(html.text)
    else:
        print('нет новых новостей') #это для наглядности, в боте не нужно 
    time.sleep(30)
    html = get_html(URL) 
    get_link(html.text)
    
def get_news(html):
    global last_name
    soup = BeautifulSoup(html, 'html.parser')
    news = soup.find_all('div', class_ = 'article__text')
    print(last_name)
    for new in news:
        print(new.get_text())
       
    
def parse(): 
    html = get_html(URL) 
    if html.status_code == 200: 
        get_link(html.text)
    else:
        print('Error')
     
#main
last_name = 'none'
parse()


'''
TG_TOKEN = "1169148923:AAGgN2JhEvTDCTOhMnmw4P6iDL2aU1nyRbY"
apihelper.proxy = {"https" : "socks5//128.199.208.93:32937"}

def message_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='test'
    )

def main():
    print('Start')

    updater = Updater(
        token=TG_TOKEN,
        url
        use_context=True,
    )

    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
'''
