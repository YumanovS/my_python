#!/usr/bin/env python
# coding: utf-8

# In[16]:


value = input("Введите атомный номер: ")
if value:
    number = float(value)
    if number == 3:
        print("Li")
    elif  number == 25:
        print("Mn")
    elif  number == 80:
        print("Hg")
    elif  number == 17:
        print("Cl")
    else:
        print("Что это?!")
else:
    print("Введите атомный номер!")

