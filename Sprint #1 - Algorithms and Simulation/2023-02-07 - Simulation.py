#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from sci378 import *


# variables - initial values

# In[6]:


y=200
v=0
t=0


# parameters - values

# In[7]:


m=1
g=10


# In[8]:


dt=0.01


# loop the model equations
# 
# $$
# \begin{aligned}
# \frac{dy}{dt}&=v \\
# \frac{dv}{dt}&=-g
# \end{aligned}
# $$

# In[9]:


S=Storage()

S+=t,y,v
while t<10:
    
    dy=v*dt
    dv=-g*dt
    
    v=v+dv
    y=y+dy
    t=t+dt
    
    S+=t,y,v
    
t,y,v=S.arrays()


# In[12]:


plot(t,y)
ylabel('height')


# In[11]:


figure(figsize=(8,4))
subplot(2,1,1)
plot(t,y)
ylabel('height')
subplot(2,1,2)
plot(t,v)
ylabel('speed')


# In[ ]:


v=v+dv
y=y+dy
t=t+dt


v+=dv
y+=dy
t+=dt

