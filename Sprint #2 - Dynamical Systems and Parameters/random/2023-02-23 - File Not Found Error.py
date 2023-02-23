#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *


# In[2]:


from pyndamics3 import Simulation


# In[3]:


import pandas as pd


# In[4]:


data=pd.read_csv('logistic_sample_data/logistic_sample_data_0.csv')
data.head()


# 1. check the spelling
# 2. check forward slashes (correct) /   instead of backslashes (incorrect) \
# 3. where does the notebook think it is...use the pwd command

# In[5]:


pwd


# the data folder for this file is one up (parent folder) from here

# In[6]:


data=pd.read_csv('../logistic_sample_data/logistic_sample_data_0.csv')


# In[8]:


data.head()


# Do **NOT** load it like this:

# In[9]:


data=pd.read_csv('/Users/bblais/Documents/Git/Computer-Programming-for-the-Sciences-Spring-2023/Sprint #2 - Dynamical Systems and Parameters/logistic_sample_data/logistic_sample_data_0.csv')
data.head()


# In[ ]:




