#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from sci378 import *


# In[2]:


def fun(θ):
    return cos(θ)**3-sin(θ)**2


# In[3]:


θ=linspace(0,90,500)
d=fun(radians(θ))

plot(θ,d)


# In[ ]:




