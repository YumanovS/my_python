#!/usr/bin/env python
# coding: utf-8

# In[25]:


#Сейчас существуют некоторые проблемы с правильным запуском

import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://www.avito.ru/sankt-peterburg/avtomobili/gaz-ASgBAgICAUTgtg3KmSg?radius=0'
goods = []

HOST = 'https://www.port Beautifuavito.ru'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}
FILE = 'goods.csv'

#def

def get_html(url, params=None):
    r = requests.get(url, headers = HEADERS,params = params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_ = 'item__line')
    
    for item in items:
        goods.append({
            'name': item.find('a', class_ = 'snippet-link').get_text(),
            'price': item.find('span', class_ = 'snippet-price').get_text(strip = True),
            'parametrs': item.find('div', class_ = 'specific-params specific-params_block').get_text(strip = True),
            'adress': item.find('div', class_ = 'item-address').get_text(strip = True),
            'time': item.find('div', class_ = 'snippet-date-info').get_text(strip = True),
            'link': HOST + item.find('a', class_ = 'snippet-link').get('href')
        })

    

def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('span', class_ = 'pagination-item-1WyVp') 
    if pagination: 
        return int(pagination[-2].get_text()) 
    else: 
        return 1
    
#def save_file(items,path): 
#    with open(path, 'w', newline = '', encoding = 'UTF-8') as file: 
#        writer = csv.writer(file, delimiter = ';') 
#        writer.writerow(['Name', 'Price', 'Parametrs','adress','Time_Add', 'Link']) 
#        for item in items: 
#            writer.writerow([item['name'] , item['price'] , item['parametrs'] , item['adress'] , item['time'] , item['link']])


def parse(): 
    html = get_html(URL) 
    if html.status_code == 200: 
        pages_count = get_pages_count(html.text)
        for page in range(1, pages_count + 1): 
            print(f'Парсинг страницы {page} из {pages_count}...') 
            html = get_html(URL, params = {'p': page}) 
            goods.append(get_content(html.text)) 
            #save_file(goods,FILE)
    else:
        print('Error')
    print(goods) 
#main

parse()


# In[ ]:




