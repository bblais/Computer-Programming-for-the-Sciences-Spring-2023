#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from pyndamics3 import Simulation


# In[4]:


import pandas as pd


# In[8]:


data=pd.read_csv('data/vostok.icecore.co2.txt',skiprows=22,delimiter='\t',header=None)
data


# In[10]:


t_data=array(data[2])
y_data=array(data[3])

figure(figsize=(8,4))  # make small for the projector -- you don't need this line
plot(t_data,y_data,'o')


# $$
# \frac{dx}{dt}= v 
# $$
# 
# $$
# \frac{dv}{dt}= -k\cdot (x-x_o)/m
# $$

# In[19]:


sim=Simulation()
sim.add(" x' = v   ",280,plot=True)
sim.add(" v' = -k*(x-xo)/m",0)
sim.params(k=2,m=7e8,xo=230)
sim.add_data(t=t_data,x=y_data,plot=True)
sim.run(400000)


# In[ ]:




