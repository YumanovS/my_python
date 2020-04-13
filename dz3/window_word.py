#!/usr/bin/env python
# coding: utf-8

# In[13]:


from tkinter import *
from random import *

#dict

englishdict = {'cat':'кошка','dog':'собака','house':'дом', 'mouse':'мышь','car':'машина','plane':'самолет'}
word = choice(list(englishdict.keys()))

#window

window = Tk()
window.title("Перевод")
window.geometry('640x480')
window.resizable( width = False, height = False )
window[ 'bg' ] = '#ccc'

#def

def guess():
        wordf = englishdict.get(word)
        if my_word.get() == wordf:
            label_out.config(text = 'Верно')
        else:
            label_out.config(text = 'Неверно')

#event

label_text = Label(window,text = 'Слово: ', 
                  font = 'Comfortaa 20',
                 fg = '#3d3d42',
                 bg = '#ccc')
label_word = Label(window,text = word,font = 'Comfortaa 20',
                 fg = '#3d3d42',
                 bg = '#ccc')
label_text2 = Label(window, text = 'Укажите перевод: ',font = 'Comfortaa 20',
                 fg = '#3d3d42',
                 bg = '#ccc')
my_word = Entry(window)
label_out = Label(window,font = 'Comfortaa 20',
                 fg = '#3d3d42',
                 bg = '#ccc')
button_guess = Button(window, text = 'Угадать', command = guess,
                     font = 'Consolas 13',
                     bg = '#48494f',
                     fg = '#eff5c9',
                     relief = 'solid',
                     activeforeground = '#eff5c9',
                     activebackground = '#6e6f73')
button_quit = Button(window, text = 'Выход', command = window.destroy,
                    font = 'Consolas 13',
                     bg = '#48494f',
                     fg = '#eff5c9',
                     relief = 'solid',
                     activeforeground = '#eff5c9',
                     activebackground = '#6e6f73')


#pack

label_text.pack()
label_word.pack()
label_text2.pack()
my_word.pack()
label_out.pack()
button_guess.pack()
button_quit.pack()

window.mainloop()


# In[ ]:





# In[ ]:




