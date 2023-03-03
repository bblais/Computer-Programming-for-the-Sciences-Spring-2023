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


data=pd.read_excel('data/Mobile telephone service.xlsx')
data


# In[5]:


t_data=array(data['Year'])
y_data=array(data['Americans with Cellular Service (%)'])

figure(figsize=(8,4))  # make small for the projector -- you don't need this line
plot(t_data,y_data,'o')


# In[14]:


sim=Simulation()
sim.figsize=(8,4)
sim.add(" y' = a*y*(1-y/K) ",5,plot=True) # the 1 here is the initial value for x
sim.params(a=.25,K=100)
sim.add_data(t=t_data,y=y_data,plot=True)
sim.run(1990,2015)  # this is how long the simulation should run -- how large of a value of t


# In[ ]:




