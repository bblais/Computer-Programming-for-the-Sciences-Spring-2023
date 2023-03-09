#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from pyndamics3 import Simulation


# In[3]:


sim=Simulation()
sim.add(" x' = v",50)
sim.add(" v' = -g+(k*v**2)/m",(sqrt(3*5/1)))
sim.params(k=1,m=5,g=3)
sim.run(10)

t=sim.t
v=sim.v

figure(figsize=(8,4))
plot(t,v)
plot(t,(sqrt(3*5/1))*ones(len(t)),'r--')


# In[5]:


sim.v[0],sim.v[-1]


# In[6]:


sim=Simulation()
sim.add(" x' = v",50)
sim.add(" v' = -g+(k*v**2)/m",(sqrt(3*5/1)))
sim.params(k=1,m=5,g=3)
sim.run(10)

t=sim.t
v=sim.v

figure(figsize=(8,4))
plot(t,v)
plot(t,(sqrt(3*5/1))*ones(len(t)),'r--')

ylim([0,5])


# In[7]:


0.1 + 0.2


# In[10]:


.1+.2 == .3


# In[ ]:




