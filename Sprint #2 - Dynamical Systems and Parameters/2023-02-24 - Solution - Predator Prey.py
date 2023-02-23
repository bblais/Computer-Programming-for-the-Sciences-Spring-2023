#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from pyndamics3 import Simulation


# ![image.png](attachment:ec74a94b-0871-4b00-a0fa-ee16cf4c39b1.png)
# 
# ![image.png](attachment:de8b16cf-b017-4a7a-8834-9342b651fb77.png)

# In[9]:


sim=Simulation()
sim.add(" x' = α*x - β*x*y",10,plot=True)
sim.add(" y' = δ*x*y-γ*y",10,plot=True)
sim.params(α=1.1 ,β=0.4, δ=.1, γ=.4 )
sim.run(100)


# In[10]:


sim=Simulation()
sim.add(" x' = α*x - β*x*y",10)
sim.add(" y' = δ*x*y-γ*y",10)
sim.params(α=1.1 ,β=0.4, δ=.1, γ=.4 )
sim.run(100)

plot(sim.t,sim.x)
plot(sim.t,sim.y)


# In[11]:


sim=Simulation()
sim.add(" x' = α*x - β*x*y",10,plot=1)
sim.add(" y' = δ*x*y-γ*y",10,plot=1)
sim.params(α=1.1 ,β=0.4, δ=.1, γ=.4 )
sim.run(100)


# In[ ]:




