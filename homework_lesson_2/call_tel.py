#!/usr/bin/env python
# coding: utf-8

# In[6]:


code = input("Введите код города: ")
time = input("Введите продожительность переговоров (В мин): ")
def call(x,y):    
    if code:
        if time:
            x = int(code)
            y = int(time)
        if x == 343:
            return  15 * y
        elif x == 381:
            return 18 * y
        elif x == 473:
            return 13 * y
        elif x == 485:
            return 11 * y
        else:
            print("Неверный код города!")
call(code,time)

