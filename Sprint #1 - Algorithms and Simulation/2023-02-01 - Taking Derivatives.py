#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from sci378 import *


# In[2]:


def fun(x):
    return x**2-10*x+11


# In[17]:


pwd


# In[7]:


fun(-1)


# In[8]:


linspace(-5,15,11)


# In[9]:


fun(linspace(-5,15,11))


# In[11]:


figure(figsize=(6,4))
x=linspace(-5,15,100)
y=fun(x)
plot(x,y)


# In[13]:


figure(figsize=(6,4))
x=linspace(-5,15,20)
y=fun(x)
plot(x,y,'o')


# ## derivative
# 
# - run through each x value
# - get the function a little bit to the left and to the right
# - calculate the slope -- rise/run
# - keep a record of each of these calculation (collecting all of the individual calc into array)

# In[14]:


x_start=-5
x_end=15
step=0.1

S=Storage()

x=x_start
while x<=x_end:
    
    #print(x," ",end="")
    
    y_left=fun(x-step/2)
    y_right=fun(x+step/2)
    
    m=(y_right-y_left)/(step)
    
    S+=x,m
    
    x=x+step
    
print("done.")

x,m=S.arrays()


# In[16]:


figure(figsize=(6,4))

plot(x,m)

x_expected=linspace(-5,15,100)
y_expected=2*(x_expected-5)

plot(x_expected,y_expected,'r--')


# ## integral
# 
# - run through each x value
# - get the function a little bit to the left and to the right
# - calculate the area -- rectangle and a triangle
# - keep a record of each of these calculation (collecting all of the individual calc into array)

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## zeros
# 
# 
# - run through each x value
# - get the function a little bit to the left and to the right
# - check the sign -- if signs are the same, then if we multiply them we get 1, if prod signs not equal 1, then zero
# - keep a record of each of these calculation (collecting all of the individual calc into array)

# In[15]:


sign(-5)


# In[16]:


sign(9)


# In[ ]:




