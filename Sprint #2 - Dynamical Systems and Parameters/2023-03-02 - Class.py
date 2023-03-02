#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from pyndamics3 import Simulation


# In[2]:


sim=Simulation()
sim.add(" x' = v   ",5,plot=True)
sim.add(" v' = -k*x/m",0,plot=True)
sim.params(k=2,m=1)
sim.run(20)


# In[3]:


t=linspace(1990,2000,200)
x=randn(len(t))+300
plot(t,x,'o')


# In[6]:


sim=Simulation()
sim.add(" x' = v   ",5,plot=True)
sim.add(" v' = -k*(x-xo)/m",0)
sim.params(k=2,m=1,xo=5)
sim.add_data(t=t,x=x,plot=True)

sim.run(1990,2000)


# In[7]:


sim=Simulation()
sim.add(" x' = v   ",5,plot=True)
sim.add(" v' = -k*(x-xo)/m",0)
sim.params(k=2,m=1,xo=5)
sim.add_data(t=t,x=x-x.mean(),plot=True)

sim.run(1990,2000)


# In[25]:


t_data=linspace(1990,2000,200)
x_data=randn(len(t_data))+300
plot(t_data,x_data,'o')


# In[40]:


sim=Simulation()
sim.add(" x' = v   ",298,plot=True)
sim.add(" v' = -k*(x-xo)/m",0)
sim.params(k=2,m=1,xo=300)
sim.add_data(t=t_data,x=x_data,plot=True)

sim.run(1990,2000)


# In[41]:


t=sim.t
x=sim.x
plot(t,x,'b-')
plot(t_data,x_data,'bo-')


# In[45]:


# all in one cell

sim=Simulation()
sim.add(" x' = v   ",298)
sim.add(" v' = -k*(x-xo)/m",0)
sim.params(k=20,m=1,xo=300)
sim.add_data(t=t_data,x=x_data)

sim.run(1990,2000)

t=sim.t
x=sim.x
plot(t,x,'b-')
plot(t_data,x_data,'co-')


# In[46]:


get_ipython().run_line_magic('pinfo2', 'plot')


# In[ ]:





# In[ ]:





# In[30]:


plot(sim.t,sim.x,'b-')
plot(t_data,x_data,'bo-')


# In[18]:


t=sim.t
x=sim.x

plot(t,x,'b-')


# In[22]:


# plotting the fixed point

t=sim.t
x=sim.x

plot(t,x,'b-')
plot(t,300*ones(len(t)),'r--')


# In[23]:


# plotting the fixed point

t=sim.t
x=sim.x
xo=sim.xo

plot(t,x,'b-')
plot(t,xo*ones(len(t)),'r--')


# In[33]:


import pandas as pd
data=pd.read_csv('data/algiers_temp2.csv')
data


# In[36]:


t=data['Year']+(data['Month']-1)/12+(data['Day']-1)/12/30
y=data['AvgTemperature']

t=t[y>0]
y=y[y>0]
plot(t,y,'o-')


# In[ ]:




