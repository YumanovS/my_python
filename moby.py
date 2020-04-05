#!/usr/bin/env python
# coding: utf-8

# In[3]:


with open ("moby.txt", "r") as main, open("moby_clean.txt","a") as second:
    trantab1 = str.maketrans("","",".,;:-")
    trantab2 = str.maketrans({"\n":None})
    contents = main.read().lower()
    contents = contents.translate(trantab1).translate(trantab2)
    for i in contents.split():
        second.write("".join([i,"\n"]))


# In[ ]:




