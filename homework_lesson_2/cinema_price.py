#!/usr/bin/env python
# coding: utf-8

# In[17]:


film = input("Выбрать фильм: ")
date = input("Выбрать день (сегодня, завтра): ")
time = int(input("Выбрать время: "))
num_of_tic = int(input("Выбрать количество билетов: "))
if film == "Паразиты":
    if time == 12:
        price = 250 * num_of_tic
    elif time == 16:
        price = 350 * num_of_tic
    elif time == 20:
        price = 450 * num_of_tic
    if date == "завтра":
        price = price * 0.95
    elif date == "сегодня":
        price = price
    if num_of_tic > 19:
        price = price * 0.8
    else: 
        print("Некорректный ввод!")
    print("Общяя цена: " + str(price) + " руб.")
elif film == "1917":
    if time == 10:
        price = 250 * num_of_tic
    elif time == 13 or time == 16:
        price = 350 * num_of_tic
    if date == "завтра":
        price = price * 0.95
    elif date == "сегодня":
        price = price
    if num_of_tic > 19:
        price = price * 0.8
    else: 
        print("Некорректный ввод!")
    print("Общяя цена: " + str(price) + " руб.")
elif film == "Соник в кино":
    if time == 10:
        price = 350 * num_of_tic
    elif time == 14 or time == 18:
        price = 450 * num_of_tic
    if date == "завтра":
        price = price * 0.95
    elif date == "сегодня":
        price = price
    if num_of_tic > 19:
        price = price * 0.8
    else: 
        print("Некорректный ввод!")
    print("Общяя цена: " + str(price) + " руб.")
else: 
    print("Некорректный ввод!")


# In[ ]:





# In[ ]:




