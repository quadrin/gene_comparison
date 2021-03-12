#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pandas as pd
import numpy as np


# In[39]:


df = pd.read_csv('targeted genes by miR.csv', sep=',')
df = df.dropna(axis=1, how='all') #supposed to drop NANs

df


# In[278]:


"""#for formatting, ignore otherwise!

df = pd.read_csv('dataset_3_9_afternoon.csv', sep=',')
df = df.dropna(axis=1, how='all')
df = df.drop(df.index[0])
df = df.drop(df.index[0])
df.columns = df.iloc[0]
df = df.drop(df.index[0])

df"""


# In[34]:


df_no_first = df.drop(df.columns[0], axis=1)
df_no_first

common_genes = {}


# In[24]:


#ignore
""""for i in range(len(df_no_first.columns)):
    common_genes[df_no_first.columns[i]] = list(set(df[df.columns[1]]) & set(df_no_first[df_no_first.columns[i]]))


# In[35]:


#for other easier formatting

for i in range(len(df_no_first.columns)):
    common_genes[df_no_first.columns[i]] = list(set(df[df.columns[0]]) & set(df_no_first[df_no_first.columns[i]]))""""


# In[36]:


common_genes


# In[37]:


import csv

filename = "new_genes_in_common.csv"

with open(filename, 'w') as f:
    for key in common_genes.keys():
        f.write("%s, %s\n" % (key, common_genes[key]))


# In[30]:


data = pd.read_csv('new_genes_in_common.csv', error_bad_lines=False)


# In[31]:


data


# In[ ]:




