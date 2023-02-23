#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *


# In[2]:


from pyndamics3 import Simulation


# In[3]:


import pandas as pd


# In[5]:


data=pd.read_csv('logistic_sample_data/logistic_sample_data_0.csv')
data.head()


# In[9]:


t_data=array(data['t'])
y_data=array(data['y'])

figure(figsize=(8,4))  # make small for the projector -- you don't need this line
plot(t_data,y_data,'o')


# In[11]:


sim=Simulation()
sim.figsize=(8,4)
sim.add(" y' = a*y*(1-y/K) ",1,plot=True) # the 1 here is the initial value for x
sim.params(a=2,K=50)
sim.add_data(t=t_data,y=y_data,plot=True)
sim.run(0,10)  # this is how long the simulation should run -- how large of a value of t


# In[12]:


sim=Simulation()
sim.figsize=(8,4)
sim.add(" y' = a*y*(1-y/K) ",1,plot=True) # the 1 here is the initial value for x
sim.params(a=2,K=300)
sim.add_data(t=t_data,y=y_data,plot=True)
sim.run(0,10)  # this is how long the simulation should run -- how large of a value of t


# In[13]:


sim=Simulation()
sim.figsize=(8,4)
sim.add(" y' = a*y*(1-y/K) ",1,plot=True) # the 1 here is the initial value for x
sim.params(a=2,K=300)
sim.add_data(t=t_data,y=y_data,plot=True)
sim.run(0,50)  # this is how long the simulation should run -- how large of a value of t


# In[14]:


sim=Simulation()
sim.figsize=(8,4)
sim.add(" y' = a*y*(1-y/K) ",1,plot=True) # the 1 here is the initial value for x
sim.params(a=2,K=270)
sim.add_data(t=t_data,y=y_data,plot=True)
sim.run(0,50)  # this is how long the simulation should run -- how large of a value of t


# In[ ]:




