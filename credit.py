#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv
s = []
un_s = []
with open("opendata.stat.txt", "r", encoding = "UTF-8") as statistic:
        stat = list(csv.reader(statistic))
        for i in stat:
            if i[0] == "name ":
                continue
            else:
                if i[0] == 'Количество заявок на потребительские кредиты' and i[2][0:4] == '2017':
                    s.append(i[1])
        un_s = list(set(s))
        d = dict(zip(un_s,[0 for j in un_s]))
        for i in stat:
            if i[0] == "name ":
                continue
            else:
                if i[0] == 'Количество заявок на потребительские кредиты' and i[2][0:4] == '2017':
                     d[i[1]] += int(i[3])
        del  d['Россия']
print(tuple(reversed(max(zip( d.values(), d.keys())))))


# In[ ]:




