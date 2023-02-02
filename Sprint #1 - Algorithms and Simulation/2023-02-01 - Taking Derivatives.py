#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from sci378 import *


# In[3]:


def fun(x):
    return x**2-10*x+11


# In[4]:


pwd


# In[5]:


fun(-1)


# In[6]:


linspace(-5,15,11)


# In[7]:


fun(linspace(-5,15,11))


# In[8]:


figure(figsize=(6,4))
x=linspace(-5,15,100)
y=fun(x)
plot(x,y)


# In[9]:


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

# In[13]:


x_start=-5
x_end=15
step=1

S=Storage()

x=x_start
while x<=x_end:
    
    # print(x," ",end="")
    
    y_left=fun(x-step/2)
    y_right=fun(x+step/2)
    
    m=(y_right-y_left)/(step) # rise over run
    
    S+=x,m   # saving the result for later
    
    x=x+step
    
print("done.")

x,m=S.arrays()  # give me the saved results as two arrays


# In[14]:


x


# In[15]:


m


# In[16]:


figure(figsize=(6,4))

plot(x,m,'b-')  # the numerical derivative

x_expected=linspace(-5,15,100)
y_expected=2*(x_expected-5)  # this is the expected from calculus

plot(x_expected,y_expected,'r--')


# ## integral
# 
# - run through each x value
# - get the function a little bit to the left and to the right
# - calculate the area -- rectangle and a triangle
# - keep a running sum
# - keep a record of each of these calculation (collecting all of the individual calc into array)

# In[17]:


x_start=-5
x_end=15
step=0.1

S=Storage()

x=x_start
total_area=0
while x<=x_end:
        
    y_left=fun(x-step/2)
    y_right=fun(x+step/2)
    
    area_rect=y_right*step
    area_tri=(1/2)*step*(y_left-y_right)
    
    total_area=total_area+area_rect+area_tri
    
    
    S+=x,total_area   # saving the result for later
    
    x=x+step
    
print("done.")

x,total_area=S.arrays()  # give me the saved results as two arrays


# In[19]:


figure(figsize=(6,4))

plot(x,total_area,'b-')  # the numerical derivative

xx=x_expected=linspace(-5,15,100)
y_expected=xx**3/3 + 10*xx**2/2 + 11*xx -5  # this is the expected from calculus

plot(x_expected,y_expected,'r--')


# In[ ]:





# In[ ]:





# ## zeros
# 
# 
# - run through each x value
# - get the function a little bit to the left and to the right
# - check the sign -- if signs are the same, then if we multiply them we get 1, if prod signs not equal 1, then zero
# - keep a record of each of these calculation (collecting all of the individual calc into array)

# In[20]:


sign(-5)


# In[21]:


sign(9)


# In[24]:


x_start=-5
x_end=15
step=0.01

S=Storage()

x=x_start
while x<=x_end:
    
    # print(x," ",end="")
    
    y_left=fun(x-step/2)
    y_right=fun(x+step/2)
    
    if sign(y_left)!=sign(y_right):
        S+=x,y_left, y_right  # saving the result for later
    
    x=x+step
    
print("done.")

x,y_left, y_right=S.arrays()  # give me the saved results as two arrays

x,y_left, y_right


# In[ ]:




