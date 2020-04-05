#!/usr/bin/env python
# coding: utf-8

# In[ ]:


while True:
    a, b  =  0, 0
    try:
        try:
            a, b = input('Input 2 numbers ').split()
        except ValueError:
            print("Input two numbers!")
            continue
        a, b  = float(a) , float(b)
    except ValueError:
        print("Input Error!")
        continue
    c = input('Input operator ')
    if c == "+":
        print(a + b)
    elif c == "-":
        print(a - b)
    elif c == "*":
        print(a * b)
    elif c == "/":
        try:
            print(a / b)
        except ZeroDivisionError:
            print("Zero Division Error!")
            continue
    else:
        print("Input operator Error!")
        continue


# In[ ]:




