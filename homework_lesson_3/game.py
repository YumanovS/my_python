#!/usr/bin/env python
# coding: utf-8

# In[23]:


number = int(input("Введите число: "))
def game(number):
    import random
    a = random.randint(1,4)
    while number != a:
        if number > a:
            print("Меньше")
        elif number < a:
            print("Больше")
        number = int(input("Введите число: "))
    print("Победа!")
game(number)  

