#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from sci378 import *


# In[3]:


import pandas as pd


# In[6]:


pwd


# In[5]:


data=pd.read_excel('data/object1_data.xlsx')
data


# In[7]:


data=pd.read_excel('/Users/bblais/Documents/Git/Computer-Programming-for-the-Sciences-Spring-2023/Sprint #1 - Algorithms and Simulation/data/object1_data.xlsx')
data


# In[8]:


t=array(data['t'])
y=array(data['y'])


# In[10]:


t,y


# In[14]:


t_model=linspace(0,.6,100)
y_model=-3*t_model+2

plot(t,y,'o')
plot(t_model,y_model,'-')


# In[ ]:




