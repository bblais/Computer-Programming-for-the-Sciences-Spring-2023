#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from sci378 import *


# In[2]:


x=linspace(10,30,100)

y1=randn(len(x))
y2=randn(len(x))+100


plot(x,y1,'o')
plot(x,y2,'s')


# In[3]:


x=linspace(10,30,100)

y1=randn(len(x))
y2=randn(len(x))+100

subplot(2,1,1)
plot(x,y1,'o')
subplot(2,1,2)
plot(x,y2,'s')


# In[6]:


x=linspace(10,30,100)

y1=randn(len(x))
y2=randn(len(x))+100

plot(x,y1,'bo-')
twinx()
plot(x,y2,'rs-')


# In[8]:


plot(x,y1,'o-',color='#587246')


# In[ ]:




