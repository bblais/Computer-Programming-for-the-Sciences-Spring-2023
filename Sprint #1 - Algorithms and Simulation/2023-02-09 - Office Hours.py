#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from sci378 import *


# In[3]:


x=5
x


# In[4]:


x=x+7
x


# In[6]:


x=array([1,2,3,4,5])


# In[7]:


2*x


# What does linspace do?  it makes an array of linearly spaced values from a start to an end, given the number of points to have in the array.

# In[8]:


linspace(3,8,10)  # with 10 points


# In[15]:


linspace(3,8,7)  # with 7 points


# In[16]:


linspace(3,8,4)  # with 4 points


# In[ ]:





# In[12]:


x=linspace(-10,10,1000)
y=x**2-2*x+3
plot(x,y)


# In[ ]:




