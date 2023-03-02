#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from pyndamics3 import Simulation


# In[2]:


sim=Simulation()
sim.add(" x' = v   ",5,plot=True)
sim.add(" v' = -k*x/m",0,plot=True)
sim.params(k=2,m=1)
sim.run(20)


# In[3]:


t=linspace(1990,2000,200)
x=randn(len(t))+300
plot(t,x,'o')


# In[6]:


sim=Simulation()
sim.add(" x' = v   ",5,plot=True)
sim.add(" v' = -k*(x-xo)/m",0)
sim.params(k=2,m=1,xo=5)
sim.add_data(t=t,x=x,plot=True)

sim.run(1990,2000)


# In[7]:


sim=Simulation()
sim.add(" x' = v   ",5,plot=True)
sim.add(" v' = -k*(x-xo)/m",0)
sim.params(k=2,m=1,xo=5)
sim.add_data(t=t,x=x-x.mean(),plot=True)

sim.run(1990,2000)


# In[13]:


sim=Simulation()
sim.add(" x' = v   ",290,plot=True)
sim.add(" v' = -k*(x-xo)/m",0)
sim.params(k=2,m=1,xo=300)
sim.add_data(t=t,x=x,plot=True)

sim.run(1990,2000)


# In[ ]:




