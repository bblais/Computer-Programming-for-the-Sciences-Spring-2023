#!/usr/bin/env python
# coding: utf-8

# In[10]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *


# In[4]:


from numpy import sin, cos


# In[8]:


import numpy as np


# In[3]:


sin(90)


# In[5]:


from numpy import *


# In[7]:


sin(radians(90))


# In[9]:


np.sin(np.radians(90))


# In[11]:


linspace(2,10,23)


# In[12]:


x=linspace(2,10,23)


# In[13]:


x


# In[14]:


5*x


# In[16]:


x=linspace(2,10,23)
y=2*x+3
plot(x,y,'-o')


# In[24]:


x=linspace(2,10,500)
y=5*x**2-2*x+3
plot(x,y,'-',label='$5x^2-2x+3$')

plot(x,2*y,'-',label='$10x^2-4x+6$')
xlabel('Time')
ylabel('Bacon')
legend()


# In[25]:


from sci378 import *


# In[26]:


x=linspace(2,10,500)
y=5*x**2-2*x+3
plot(x,y,'-',label='$5x^2-2x+3$')

plot(x,2*y,'-',label='$10x^2-4x+6$')
xlabel('Time')
ylabel('Bacon')
legend()


# In[ ]:




