#!/usr/bin/env python
# coding: utf-8

# In[26]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from sci378 import *


# In[27]:


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

# The function is 
# $$
# f(x)=x^2-10x+11
# $$
# 
# The derivative of the function
# $$
# \frac{df(x)}{dx}=2x-10
# $$

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

# The function is 
# $$
# f(x)=x^2-10x+11
# $$
# 
# The integral of the function
# $$
# \begin{aligned}
# \int_{x_{\rm start}}^{x} f(x')dx'&=\left. \frac{x^3}{3}-\frac{10x^2}{2}+11x \right|_{x_{\rm start}}^{x}\\
# &=\frac{x^3}{3}-\frac{10x^2}{2}+11x - \left(\frac{x_{\rm start}^3}{3}-\frac{10x_{\rm start}^2}{2}+11x_{\rm start} \right)
# \end{aligned}
# $$

# In[30]:


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


# the following plot is clearly wrong, so let's see if we can debug things.

# In[31]:


figure(figsize=(6,4))

plot(x,total_area,'b-')  # the numerical integral

xx=x_expected=linspace(-5,15,100)
y_expected=xx**3/3 + 10*xx**2/2 + 11*xx -5  # this is the expected from calculus

plot(x_expected,y_expected,'r--')


# ## debugging

# In[32]:


x_start=-5
x_end=15
step=0.1

S=Storage()

x=x_start
total_area=0
while x<=x_end:
        
    y_left=fun(x-step/2)
    y_right=fun(x+step/2)
    
    area_rect=y_left*step
    area_tri=(1/2)*step*(y_right-y_left)
    
    total_area=total_area+area_rect+area_tri
    
    
    S+=x,total_area   # saving the result for later
    
    x=x+step
    
print("done.")

x,total_area=S.arrays()  # give me the saved results as two arrays


# In[36]:


figure(figsize=(6,4))

plot(x,total_area,'b-')  # the numerical integral

xx=x_expected=linspace(-5,15,100)
y_expected=xx**3/3 - 10*xx**2/2 + 11*xx -(x_start**3/3-10*x_start**2/2+11*x_start)  # this is the expected from calculus

plot(x_expected,y_expected,'r--')


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

# In[20]:


sign(-5)


# In[21]:


sign(9)


# In[25]:


x_start=-5
x_end=15
step=0.01

S=Storage()

x=x_start
number_of_steps=0
while x<=x_end:
    
    # print(x," ",end="")
    
    y_left=fun(x-step/2)
    y_right=fun(x+step/2)
    
    if sign(y_left)!=sign(y_right):
        S+=x,y_left, y_right  # saving the result for later
    
    x=x+step
    number_of_steps=number_of_steps+1
    
print("done...",number_of_steps)

x,y_left, y_right=S.arrays()  # give me the saved results as two arrays

x,y_left, y_right


# In[ ]:




