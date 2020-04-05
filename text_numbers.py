#!/usr/bin/env python
# coding: utf-8

# In[10]:


try:
     with open("text.txt","r") as main, open("update_text.txt","w") as update:
        lines = main.readlines()
        append = "".join([str(i+1) + " " + lines[i] for i in range(len(lines))])
        update.write(append)
except Exception as b:
    print(b)


# In[ ]:




