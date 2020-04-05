#!/usr/bin/env python
# coding: utf-8

# In[1]:


def create_csv(file,cont):
    try:
        with open(file,"w") as file:
            a = list(map(lambda b: ",".join(b),cont))
            d = "name, adress, age\n" + "\n".join(a)
            file.write(d)
    except Exception as с:
        print(с)


# In[3]:


cont = [("Георгий", "Невский проспект", "22"),("Иван", "пр. Ветеранов", "21")]
try:
    with open("csf_file.txt","w", encoding = 'UTF-8') as file:
        a = list(map(lambda b: ",".join(b),cont))
        d = "name, adress, age\n" + "\n".join(a)
        file.write(d)
except Exception as с:
     print(с)


# In[ ]:




