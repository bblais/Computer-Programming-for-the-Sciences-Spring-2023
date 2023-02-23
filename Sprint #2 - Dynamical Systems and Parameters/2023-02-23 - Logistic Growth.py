#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *


# In[2]:


from pyndamics3 import Simulation


# In[7]:


sim=Simulation()
sim.figsize=(8,4)
sim.add(" x' = a*x*(1-x/K) ",1,plot=True) # the 1 here is the initial value for x
sim.params(a=2,K=50)
sim.run(0,10)  # this is how long the simulation should run -- how large of a value of t


# ## plotting the result manually so that you have control

# In[10]:


t=sim.t
x=sim.x

figure(figsize=(8,4))  # make small for the projector -- you don't need this line
plot(t,x)
xlabel('time')
ylabel('population')


# ## parameter exploration

# In[12]:


figure(figsize=(8,4))  # make small for the projector -- you don't need this line

for K in [10,20,30,40]:

    sim=Simulation()
    sim.add(" x' = a*x*(1-x/K) ",1) # the 1 here is the initial value for x
    sim.params(a=2,K=K)
    sim.run(0,10)  # this is how long the simulation should run -- how large of a value of t
    
    plot(sim.t,sim.x,label=f"K={K}")
    
legend()
xlabel('time')
ylabel('population')


# In[13]:


figure(figsize=(8,4))  # make small for the projector -- you don't need this line

for K in [10,20,30,40]:

    sim=Simulation()
    sim.add(" x' = a*x*(1-x/K) ",1) # the 1 here is the initial value for x
    sim.params(a=2,K=K)
    sim.run(0,10)  # this is how long the simulation should run -- how large of a value of t
    
    plot(sim.t,sim.x,label=f"K={K}")
    
    legend()
    xlabel('time')
    ylabel('population')


# In[14]:



for K in [10,20,30,40]:
    figure(figsize=(8,4))  # make small for the projector -- you don't need this line

    sim=Simulation()
    sim.add(" x' = a*x*(1-x/K) ",1) # the 1 here is the initial value for x
    sim.params(a=2,K=K)
    sim.run(0,10)  # this is how long the simulation should run -- how large of a value of t
    
    plot(sim.t,sim.x,label=f"K={K}")
    
    legend()
    xlabel('time')
    ylabel('population')


# In[15]:


t=linspace(0,50,200)
y=sin(t)
z=cos(t)

plot(t,y)
plot(t,z)


# ## two variables on the same plot

# In[16]:


sim=Simulation()
sim.figsize=(8,4)
sim.add(" x' = a*x*(1-x/K) ",1,plot=True) # the 1 here is the initial value for x
sim.add(" y' = ay*x*(1-y/Ky) ",2,plot=True) # the 1 here is the initial value for y
sim.params(a=2,K=50,ay=1,Ky=100)
sim.run(0,10)  # this is how long the simulation should run -- how large of a value of t


# In[17]:


sim=Simulation()
sim.figsize=(8,4)
sim.add(" x' = a*x*(1-x/K) ",1,plot=1) # the 1 here is the initial value for x
sim.add(" y' = ay*x*(1-y/Ky) ",2,plot=1) # the 1 here is the initial value for y
sim.params(a=2,K=50,ay=1,Ky=100)
sim.run(0,10)  # this is how long the simulation should run -- how large of a value of t


# In[18]:


sim=Simulation()
sim.figsize=(8,4)
sim.add(" x' = a*x*(1-x/K) ",1) # the 1 here is the initial value for x
sim.add(" y' = ay*x*(1-y/Ky) ",2) # the 1 here is the initial value for y
sim.params(a=2,K=50,ay=1,Ky=100)
sim.run(0,10)  # this is how long the simulation should run -- how large of a value of t


# In[20]:


figure(figsize=(8,4))  # make small for the projector -- you don't need this line
plot(sim.t,sim.x)
plot(sim.t,sim.y)


# ## For greek symbols
# 
# 
# 1. type name with a backslash ---   \alpha
# 2. hit the **tab** key

# In[ ]:


\alpha
α


# In[ ]:




