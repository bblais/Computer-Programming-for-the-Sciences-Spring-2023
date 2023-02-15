#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from sci378 import *


# $$
# \frac{dy}{dt} =  \frac{1}{2}{{\bf{e}}^{\frac{t}{2}}}\sin \left( {5t} \right) + 5{{\bf{e}}^{\frac{t}{2}}}\cos \left( {5t} \right)\hspace{0.25in}y\left( 0 \right) = 0
# $$

# The solution is $y\left( t \right) = {{\bf{e}}^{\frac{t}{2}}}\sin \left( {5t} \right)$

# ## Variables

# In[9]:


y=0
t=0
dt=0.01


# ## parameters

# In[10]:


# none!


# ## Model equation and simulate
# 
# $$
# \frac{dy}{dt} =  \frac{1}{2}{{\bf{e}}^{\frac{t}{2}}}\sin \left( {5t} \right) + 5{{\bf{e}}^{\frac{t}{2}}}\cos \left( {5t} \right)\hspace{0.25in}y\left( 0 \right) = 0
# $$
# 
# 
# $$
# dy =  \left(\frac{1}{2}{{\bf{e}}^{\frac{t}{2}}}\sin \left( {5t} \right) + 5{{\bf{e}}^{\frac{t}{2}}}\cos \left( {5t} \right) \right) \cdot dt
# $$
# 

# In[11]:


S=Storage()

while t<10:
    
    dy=(0.5*exp(t/2)*sin(5*t)+5*exp(t/2)*cos(5*t))*dt
    
    y=y+dy
    t=t+dt
    
    S+=y,t
    
    
y,t=S.arrays()


# In[12]:


plot(t,y)


# ## compare to the solution
# 
# The solution is $y\left( t \right) = {{\bf{e}}^{\frac{t}{2}}}\sin \left( {5t} \right)$

# In[13]:


plot(t,y)


tt=linspace(0,10,500)
yy=exp(tt/2)*sin(5*tt)
plot(tt,yy,'r--')


# In[ ]:




