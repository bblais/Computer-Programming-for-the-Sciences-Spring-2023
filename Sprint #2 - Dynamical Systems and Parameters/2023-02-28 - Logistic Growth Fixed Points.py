#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *


# In[2]:


from pyndamics3 import Simulation


# In[27]:


sim=Simulation()
sim.figsize=(8,4)
sim.add(" x' = a*x*(1-x/K) ",1,plot=True) # the 1 here is the initial value for x
sim.params(a=2,K=20)
sim.run(0,10)  # this is how long the simulation should run -- how large of a value of t


# this plot has the wrong K, because I put the value 50 in manually...

# In[28]:


t=sim.t
x=sim.x

figure(figsize=(8,4))  # make small for the projector -- you don't need this line
plot(t,x)
xlabel('time')
ylabel('population')

plot(t,50*ones(len(t)),'r--')  # make sure the y value (fixed point) has the same shape as the x value (time)
plot(t,0*ones(len(t)),'r--')


# this plot uses the correct K because I pull the value of K from the simulation using `K=sim.K`

# In[29]:


t=sim.t
x=sim.x

K=sim.K

figure(figsize=(8,4))  # make small for the projector -- you don't need this line
plot(t,x)
xlabel('time')
ylabel('population')

plot(t,K*ones(len(t)),'r--')  # make sure the y value (fixed point) has the same shape as the x value (time)
plot(t,0*ones(len(t)),'r--')


# ## Are these actual fixed points -- set the initial value

# In[13]:


sim=Simulation()
sim.figsize=(8,4)
sim.add(" x' = a*x*(1-x/K) ",0) # the initial value for x
sim.params(a=2,K=50)
sim.run(0,10)  # this is how long the simulation should run -- how large of a value of t



t=sim.t
x=sim.x

figure(figsize=(8,4))  # make small for the projector -- you don't need this line
plot(t,x)
xlabel('time')
ylabel('population')

plot(t,50*ones(len(t)),'r--') # make sure the y value (fixed point) has the same shape as the x value (time)
plot(t,0*ones(len(t)),'r--')

plot([0,10],[0,0],'g:')


# In[9]:


sim=Simulation()
sim.figsize=(8,4)
sim.add(" x' = a*x*(1-x/K) ",50) # the initial value for x
sim.params(a=2,K=50)
sim.run(0,10)  # this is how long the simulation should run -- how large of a value of t



t=sim.t
x=sim.x

figure(figsize=(8,4))  # make small for the projector -- you don't need this line
plot(t,x)
xlabel('time')
ylabel('population')

plot(t,50*ones(len(t)),'r--') # make sure the y value (fixed point) has the same shape as the x value (time)
plot(t,0*ones(len(t)),'r--')


# ## Testing stability

# In[16]:


sim=Simulation()
sim.figsize=(8,4)
sim.add(" x' = a*x*(1-x/K) ",50) # the initial value for x
sim.params(a=2,K=50)
sim.run(0,10)  # this is how long the simulation should run -- how large of a value of t



t=sim.t
x=sim.x

figure(figsize=(8,4))  # make small for the projector -- you don't need this line
plot(t,x)
xlabel('time')
ylabel('population')

plot(t,50*ones(len(t)),'r--') # make sure the y value (fixed point) has the same shape as the x value (time)
plot(t,0*ones(len(t)),'r--')


# ### aside on ones

# In[10]:


ones(5)


# In[11]:


ones(10)


# In[12]:


6*ones(10)


# In[14]:


6*ones(len(t))


# ## back to stability

# In[17]:


sim=Simulation()
sim.figsize=(8,4)
sim.add(" x' = a*x*(1-x/K) ",50.1) # the initial value for x
sim.params(a=2,K=50)
sim.run(0,10)  # this is how long the simulation should run -- how large of a value of t



t=sim.t
x=sim.x

figure(figsize=(8,4))  # make small for the projector -- you don't need this line
plot(t,x)
xlabel('time')
ylabel('population')

plot(t,50*ones(len(t)),'r--') # make sure the y value (fixed point) has the same shape as the x value (time)
# plot(t,0*ones(len(t)),'r--') # not plotting the other fixed point


# In[18]:


sim=Simulation()
sim.figsize=(8,4)
sim.add(" x' = a*x*(1-x/K) ",50-0.1) # the initial value for x
sim.params(a=2,K=50)
sim.run(0,10)  # this is how long the simulation should run -- how large of a value of t



t=sim.t
x=sim.x

figure(figsize=(8,4))  # make small for the projector -- you don't need this line
plot(t,x)
xlabel('time')
ylabel('population')

plot(t,50*ones(len(t)),'r--') # make sure the y value (fixed point) has the same shape as the x value (time)
# plot(t,0*ones(len(t)),'r--') # not plotting the other fixed point


# since it goes towards the FP in both cases, this is a stable fixed point.

# ## Random other system

# In[20]:


sim=Simulation()
sim.figsize=(8,4)
sim.add(" y' = -γ*y ",10,plot=True) # the initial value for y
sim.params(γ=1)
sim.run(0,10)  # this is how long the simulation should run -- how large of a value of t


# In[ ]:




