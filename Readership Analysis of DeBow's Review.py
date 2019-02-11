
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


from datascience import *


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')


# In[9]:


data = "https://raw.githubusercontent.com/cameronpwright/hist-119-research/master/readership%20of%20de%20bow's%20review%20csv.csv"


# In[11]:


DeBow_Readership = Table.read_table(data)


# In[12]:


DeBow_Readership.show()


# In[17]:


DeBow_Readership = DeBow_Readership.relabeled('Unnamed: 2', 'County').relabeled('Unnamed: 3', 'State').relabeled('Unnamed: 4', 'Age').relabeled('Unnamed: 5', 'Occupation').relabeled('Unnamed: 6','Real Estate ($)').relabeled('Unnamed: 7', 'Personal Estate ($)').relabeled('Unnamed: 8', 'Slaves (#)')


# In[18]:


DeBow_Readership


# In[32]:


DeBow_Readership.drop('Unnamed: 9').drop('Unnamed: 10').drop('Unnamed: 11')


# In[33]:


DeBow_Readership.num_rows


# In[34]:


debow = DeBow_Readership.take(np.arange(2,1497,1))


# In[63]:


debow = debow.drop('Unnamed: 9').drop('Unnamed: 10').drop('Unnamed: 11')


# In[64]:


debow.sort('Slaves (#)', descending = True).show()


# In[66]:


non_slaveholders = debow.where("Slaves (#)", are.equal_to('nan'))


# In[70]:


non_slaveholders.sort('Personal Estate ($)', descending = True).show()


# In[72]:


percentage_non_slaveholders = non_slaveholders.num_rows/debow.num_rows
percentage_non_slaveholders


# In[73]:


farmers = non_slaveholders.where("Occupation", are.equal_to('Farmer'))
farmers


# In[75]:


percentage_farmers = farmers.num_rows/non_slaveholders.num_rows
percentage_farmers


# In[77]:


merchants = non_slaveholders.where('Occupation', are.equal_to('Merchant'))
merchants


# In[79]:


percent_merchants = merchants.num_rows / non_slaveholders.num_rows
percent_merchants

