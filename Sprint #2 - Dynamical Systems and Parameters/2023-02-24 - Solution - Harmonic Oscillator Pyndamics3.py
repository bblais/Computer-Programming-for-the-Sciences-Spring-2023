#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from pyndamics3 import Simulation


# $$
# \frac{dx}{dt}= v 
# $$
# 
# $$
# \frac{dv}{dt}= -k\cdot x/m
# $$

# In[3]:


sim=Simulation()
sim.add(" x' = v   ",5,plot=True)
sim.add(" v' = -k*x/m",0,plot=True)
sim.params(k=2,m=1)
sim.run(20)


# ## parameter exploration

# In[5]:


for k in [1,2,3,4]:
    sim=Simulation()
    sim.add(" x' = v   ",5)
    sim.add(" v' = -k*x/m",0)
    sim.params(k=k,m=1)
    sim.run(20)
    
    
    t=sim.t
    v=sim.v
    
    plot(t,v,label=f"k={k}")
    
legend()
xlabel('Time [s]')
ylabel('Velocity [m]')
    
    


# In[ ]:




