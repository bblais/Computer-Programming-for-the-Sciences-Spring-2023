#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from pyndamics3 import Simulation


# ![image.png](attachment:ec74a94b-0871-4b00-a0fa-ee16cf4c39b1.png)
# 

# Fixed points
# 
# $$
# \frac{dx}{dt} = \alpha x - \beta xy = x (\alpha - \beta y)=0
# $$
# 
# $$
# \frac{dy}{dt} = \delta xy - \gamma y = y (\delta x - \gamma)= 0 
# $$

# Fixed points
# 
# $$
# x=0, y=0
# $$
# 
# $$
# x=\gamma/\delta, y=\alpha/\beta
# $$

# In[2]:


sim=Simulation()
sim.add(" x' = α*x - β*x*y",10)
sim.add(" y' = δ*x*y-γ*y",10)
sim.params(α=1.1 ,β=0.4, δ=.1, γ=.4 )
sim.run(100)


# In[5]:


figure(figsize=(8,4))
plot(sim.t,sim.x,label='Prey')
plot(sim.t,sim.y,label='Predator')
legend()


# In[9]:


α=1.1
β=0.4
δ=.1
γ=.4 


sim=Simulation()
sim.add(" x' = α*x - β*x*y",γ/δ)
sim.add(" y' = δ*x*y-γ*y",α/β)
sim.params(α=α ,β=β, δ=δ, γ=γ )
sim.run(100)

figure(figsize=(8,4))
plot(sim.t,sim.x,label='Prey')
plot(sim.t,sim.y,label='Predator')
legend()


# In[10]:


α=1.1
β=0.4
δ=.1
γ=.4 


sim=Simulation()
sim.add(" x' = α*x - β*x*y",0)
sim.add(" y' = δ*x*y-γ*y",0)
sim.params(α=α ,β=β, δ=δ, γ=γ )
sim.run(100)

figure(figsize=(8,4))
plot(sim.t,sim.x,label='Prey')
plot(sim.t,sim.y,label='Predator')
legend()


# In[14]:


α=1.1
β=0.4
δ=.1
γ=.4 


sim=Simulation()
sim.add(" x' = α*x - β*x*y",γ/δ+1)
sim.add(" y' = δ*x*y-γ*y",α/β+1)
sim.params(α=α ,β=β, δ=δ, γ=γ )
sim.run(100)

figure(figsize=(8,4))
plot(sim.t,sim.x,'b-',label='Prey')
plot(sim.t,sim.y,'m-',label='Predator')

plot(sim.t,γ/δ*ones(len(sim.t)),'b--')
plot(sim.t,α/β*ones(len(sim.t)),'m--')


legend()


# In[16]:


α=1.1
β=0.4
δ=.1
γ=.4 


sim=Simulation()
sim.add(" x' = α*x - β*x*y",0+.1)
sim.add(" y' = δ*x*y-γ*y",0+.1)
sim.params(α=α ,β=β, δ=δ, γ=γ )
sim.run(100)

figure(figsize=(8,4))
plot(sim.t,sim.x,'b-',label='Prey')
plot(sim.t,sim.y,'m-',label='Predator')

plot(sim.t,γ/δ*ones(len(sim.t)),'b--')
plot(sim.t,α/β*ones(len(sim.t)),'m--')


legend()


# In[ ]:




