#!/usr/bin/env python
# coding: utf-8

# In[2]:


list1=[1,2,3,4,5,7,6]

list2=["a","b","c","d","e"]

res = {}
for key in list1:
    for value in list2:
        res[key] = value
        list2.remove(value)
        break


# In[4]:


print ("dictionary oytput is :" + str(res))


# In[ ]:




