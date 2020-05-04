#import модулей
import requests
from bs4 import BeautifulSoup
import csv
import time

URL = 'https://ria.ru/economy/' #ссылка на сайт
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
} 



#def

# последняя новость
def get_last_name(html):
    soup = BeautifulSoup(html, 'html.parser')
    name = soup.find('a', class_ = 'list-item__title color-font-hover-only').get_text()
    # name - последняя новость на сайте
    return name

# подключение к сайту через requests
def get_html(url, params=None):
    r = requests.get(url, headers = HEADERS,params = params)
    return r
# получение последней новости с сайта 
def get_link(html):
    global last_name 
    global URL
    soup = BeautifulSoup(html, 'html.parser')
    #название новости
    name = soup.find('a', class_ = 'list-item__title color-font-hover-only').get_text()
    # ссылка на новость
    link = soup.find('a', class_ = 'list-item__title color-font-hover-only').get('href')
    # время новости
    time_post = soup.find('div',class_ = 'list-item__date').get_text(),
    #новая ссылка на сайт с самой новостью
    html = get_html(link)
    # проверка последней новости (если новая новость, то она будет публиковаться)
    if last_name != name:
        last_name = name
        print(time_post)
        get_news(html.text)
    else:
        print('нет новых новостей') #это для наглядности, в боте не нужно 
    # вызов функии каждые 30 сек
    time.sleep(30)
    html = get_html(URL) 
    get_link(html.text)
    
def get_news(html):
    global last_name
    soup = BeautifulSoup(html, 'html.parser')
    # все абзацы текста новости 
    news = soup.find_all('div', class_ = 'article__text')
    print(last_name)
    # пробегаем циклом все абзацы новости соединяются вместе
    for new in news:
        print(new.get_text())
       
 # основная функция 
def parse(): 
    html = get_html(URL) 
    # проверка подлючения
    if html.status_code == 200: 
        # если подключение есть, то выполняем функции
        get_link(html.text)
    else:
        print('Error')
     
 #main
last_name = 'none'
# запускаем основную функцию
parse()
