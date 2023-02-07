#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from sci378 import *


# In[13]:


x=linspace(0,1,100)


# In[14]:


y=sin(5*x)


# In[18]:


figure(figsize=(6,4))
plot(x,y)


# In[17]:


x2=linspace(0,1,200)
y=sin(10*x2)
figure(figsize=(6,4))
plot(x2,y)


# In[ ]:




