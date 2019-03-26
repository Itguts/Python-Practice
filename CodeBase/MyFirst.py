#!/usr/bin/env python
# coding: utf-8

# <h3>MyFirst Notebook</h3>

# In[ ]:


#Print name by taking input

name = input("Enter name")
print("Hello "+name)


# In[ ]:


name


# In[2]:


get_ipython().run_line_magic('lsmagic', '')


# In[ ]:


print("Meon")


# In[1]:


get_ipython().system('pip list')


# In[3]:


get_ipython().run_line_magic('pwd', '')


# In[4]:


get_ipython().run_line_magic('ls', '')


# In[7]:


get_ipython().run_line_magic('ls', '=my')


# In[3]:


get_ipython().system('matplotlib isline')




# In[4]:


get_ipython().run_cell_magic('HTML', '', '<h4>Hi..</h4>')


# In[8]:


get_ipython().run_cell_magic('timeit', '', '## to check the time taken\nsquare_even = [n*n for n in range(1000)]')


# In[13]:


import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(10,5))

df


# In[15]:


get_ipython().run_line_magic('config', 'IPCompleter.greedy=True')


# In[2]:


pwd


# In[4]:


x = "x"
get_ipython().run_line_magic('clear', '')

