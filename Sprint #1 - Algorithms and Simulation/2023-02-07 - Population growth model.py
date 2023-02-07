#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from sci378 import *


# $$
# \frac{dp}{dt}=a\cdot p\cdot (1-p/K)
# $$
# 
# $$
# \frac{dp}{dt}=a\cdot p\cdot (1-p/K)+B
# $$
# 

# In[3]:


p=2
t=0

a=1
K=10

dt=0.01

S=Storage()

while t<10:
    
    dp=(a*p*(1-p/K))*dt
    
    p=p+dp
    t=t+dt
    
    S+=t,p
    
    
t,p=S.arrays()
    
    


# In[5]:


figure(figsize=(10,4))
plot(t,p)


# In[8]:


figure(figsize=(10,4))

p=2
t=0

a=1
K=10

dt=0.01

S=Storage()

while t<10:
    
    dp=(a*p*(1-p/K))*dt
    
    p=p+dp
    t=t+dt
    
    S+=t,p
    
    
t,p=S.arrays()
    

plot(t,p,label=f'a={a}')


#====================

p=2
t=0

a=2
K=10

dt=0.01

S=Storage()

while t<10:
    
    dp=(a*p*(1-p/K))*dt
    
    p=p+dp
    t=t+dt
    
    S+=t,p
    
    
t,p=S.arrays()
    

plot(t,p,label=f'a={a}')

#====================

p=2
t=0

a=0.5
K=10

dt=0.01

S=Storage()

while t<10:
    
    dp=(a*p*(1-p/K))*dt
    
    p=p+dp
    t=t+dt
    
    S+=t,p
    
    
t,p=S.arrays()
    

plot(t,p,label=f'a={a}')




legend()


# In[ ]:




