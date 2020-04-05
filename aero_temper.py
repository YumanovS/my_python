#!/usr/bin/env python
# coding: utf-8

# In[4]:


temp = {}
with open("temper.txt", "r") as file:
    for line in file:
        line = float(line.strip("\n"))
        try:
            temp[line] += 1
        except KeyError:
            temp[line] = 1
    max_temp = str(max(temp.keys()))
    min_temp = str(min(temp.keys()))
    av_temp = str(round(sum(temp.keys()) / len(temp),1))
    un_temp = str(len(temp))
print("Max: " + max_temp)
print("Min: " + min_temp)
print("Average: " + av_temp)
print("Unique: " + un_temp)


# In[ ]:




