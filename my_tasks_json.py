#!/usr/bin/env python
# coding: utf-8

# In[6]:


try:
    a = []
    while True:
        num = int(input("Input number (1 - Add new task,2 - Show tasks,3 - Save tasks): "))
        if num == 3:
            with open("new_to_do_list.json","w") as file:
                file.write(str(a))
            print('Tasks saved successfully')
            break
        elif num == 2:
            print(a)
        else:
            name = input("Input task: ")
            category = input("Input category: ")
            time = input("Input deadline: ")
            a.append({"category": category, "name": name, "time": time})
except Exception as c:
    print(c)


# In[ ]:




