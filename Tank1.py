#!/usr/bin/env python
# coding: utf-8

# In[1]:


print(3+3)


# In[2]:


2*3+100


# In[3]:


print("hello, world")


# In[4]:


"hello, world"


# In[5]:


print('Submission of homework of'+ 'John Doe')


# In[8]:


import numpy as np


# In[9]:


x = np.array([2,3,11])


# In[10]:


print(x)


# In[11]:


x = np.array([[1,2.],[0,0],[1+1j,2.]])


# In[12]:


print(x)


# In[ ]:





# In[13]:


x = np.arange(-10,10,2, dtype=float)


# In[14]:


print(x)


# In[16]:


x = np.arange(0,40,2)


# In[17]:


y=x**2


# In[18]:


dy_dx = (y[1:] - y[:-1]) / (x[1:] - x[:-1]); dy_dx


# In[19]:


dy_dx


# In[20]:


import matplotlib.pyplot as plt


# In[21]:


plt.plot(x, y, 'k-', label=r'$y(x)$')


# In[33]:


import math


# In[34]:


math.sin(20)


# In[ ]:




