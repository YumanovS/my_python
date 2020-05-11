import telebot
import requests
from bs4 import BeautifulSoup
import time


URL = 'https://ria.ru/economy/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

last_name = 'none'
'''
def get_last_name(html):
    soup = BeautifulSoup(html, 'html.parser')
    name = soup.find('a', class_='list-item__title color-font-hover-only').get_text()
    return name
'''

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_link(html):
    global a
    global last_name
    global URL
    global a
    global last_name
    soup = BeautifulSoup(html, 'html.parser')
    name = soup.find('a', class_='list-item__title color-font-hover-only').get_text()
    link = soup.find('a', class_='list-item__title color-font-hover-only').get('href')
    html = get_html(link)
    if last_name != name:
        last_name = name
        get_news(html.text)
    else:
       a = " "


def get_news(html):
    global last_name
    global a
    soup = BeautifulSoup(html, 'html.parser')
    news = soup.find_all('div', class_='article__text')
    a = a + last_name
    for new in news:
        a = a + new.get_text()

bot = telebot.TeleBot(token='1169148923:AAGgN2JhEvTDCTOhMnmw4P6iDL2aU1nyRbY', threaded=False)



a = ""

@bot.message_handler(content_types=["text"])

def get_text_messages(message):
    global URL
    global HEADERS
    global a

    html = get_html(URL)
    if html.status_code == 200:
        get_link(html.text)
    if a != ' ':
        bot.send_message(message.from_user.id,a)
    else:
        a = " "
    time.sleep(20)
    get_text_messages(message)



bot.polling(none_stop=True, interval=0)
