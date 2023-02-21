#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *


# In[3]:


from pyndamics3 import Simulation


# # Logistic growth
# 
# 
# $$
# \frac{dx}{dt} = a x (1-x/K)
# $$

# In[4]:


sim=Simulation()
sim.add(" x' = a*x*(1-x/K) ",1,plot=True) # the 1 here is the initial value for x
sim.params(a=2,K=50)
sim.run(0,10)


# ## Freefall
# 
# $$
# \frac{dx}{dt}=v
# $$
# 
# $$
# \frac{dv}{dt}=g-k/m v^2
# $$

# In[6]:


sim=Simulation()
sim.add(" x' = v ",0,plot=True)  # the 0 is the initial value for x
sim.add(" v' = g-k/m*v**2",0,plot=True) # the 0 is the initial value for v
sim.params(g=10,m=1,k=3)
sim.run(10)


# ## Parameter exploration

# In[10]:


figure(figsize=(8,4))

sim=Simulation()
sim.add(" x' = v ",0)  # the 0 is the initial value for x
sim.add(" v' = g-k/m*v**2",0) # the 0 is the initial value for v
sim.params(g=10,m=1,k=3)
sim.run(10)

plot(sim.t,sim.v)


sim=Simulation()
sim.add(" x' = v ",0)  # the 0 is the initial value for x
sim.add(" v' = g-k/m*v**2",0) # the 0 is the initial value for v
sim.params(g=10,m=1,k=.1)
sim.run(10)

plot(sim.t,sim.v)


# In[ ]:




