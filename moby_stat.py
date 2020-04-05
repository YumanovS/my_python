#!/usr/bin/env python
# coding: utf-8

# In[7]:


with open ("moby_clean.txt", "r") as file:
    contents = file.readlines()
    d = {i: contents.count(i) for i in contents}
    s = sorted(list(d.values()))
    maxf = a[:5]
    minf = a[-5:]
    fmax = [i for i in contents if d[i] == maxf[0] or d[i] == maxf[1] or d[i] == maxf[2] or d[i] == maxf[3] or d[i] == maxf[4]][:5]
    fmin =[i for i in contents if d[i] == minf[0] or d[i] == minf[1] or d[i] == minf[2] or d[i] == minf[3] or d[i] == minf[4]][:5]
    print(fmin)
    print(fmax)


# In[ ]:




