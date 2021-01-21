#!/usr/bin/env python
# coding: utf-8

# In[38]:


#adding 3 integers to the list
list = []

list.append(9)
list.append(5)
list.append(4)

print(list)


# In[41]:


#making new list with the first and last elements
element1 = list[0]
element2 = list[2]
new_list = [element1,element2]
new_list[0] = 0
del new_list[1]
print(new_list)


# In[42]:


#finding the third thing in the tuple
camping = ('c','a','m','p')
print(camping[2])


# In[61]:


#to find the index of the p in camp
if 'p' in camping:
    print(len(camping))


# In[62]:


#adding e to the list and deleting b from the list
abcde =  {'a':1,'b':2,'c':3,'d':4}
abcde['e'] = 5
del abcde['b']
print(abcde)

