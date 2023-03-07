#!/usr/bin/env python
# coding: utf-8

# Subscripts in $\LaTeX$
$$
v_max
$$
# $$
# v_max
# $$
$$
v_{max}
$$
# $$
# v_{max}
# $$
$$
v_{\rm max}
$$
# $$
# v_{\rm max}
# $$

# how about in code?  you can't do subscripts

# In[1]:


v_max=5


# In[2]:


v_0=5


# In[3]:


v0=5


# In[4]:


vmax=5


# In[7]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pyndamics3 import Simulation


# with `plot=True` each variable gets its own figure

# In[10]:


sim=Simulation()
sim.add("S'=-β*S*I/N",100,plot=True)
sim.add("I'=+β*S*I/N-γ*I",1,plot=True)
sim.add("R'=+γ*I",0,plot=True)
sim.add("N=S+I+R",plot=True)
sim.params(β=2,γ=1)
sim.run(20)


# if you use a number, like `plot=1`, then that specifies which figure to draw and variables with the same figure number get drawn on the same figure

# In[11]:


sim=Simulation()
sim.add("S'=-β*S*I/N",100,plot=1)
sim.add("I'=+β*S*I/N-γ*I",1,plot=1)
sim.add("R'=+γ*I",0,plot=1)
sim.add("N=S+I+R",plot=1)
sim.params(β=2,γ=1)
sim.run(20)


# the number before the `plot=` is the initial value.

# In[13]:


sim=Simulation()
sim.add("S'=-β*S*I/N",50,plot=1)
sim.add("I'=+β*S*I/N-γ*I",1,plot=1)
sim.add("R'=+γ*I",10,plot=1)
sim.add("N=S+I+R",plot=1)
sim.params(β=2,γ=1)
sim.run(20)


# In[ ]:


sim.add("v'= 5*v_max")
sim.params(v_max=10)

