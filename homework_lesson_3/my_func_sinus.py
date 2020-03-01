#!/usr/bin/env python
# coding: utf-8

# In[4]:


def my_func_sinus(x):
    import math
    if 0.2 <= x <= 0.9:
        return  math.sin(x)
    else: 
        return 1
x = float(input("Введите x: "))
my_func_sinus(x)

