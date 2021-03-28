#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[ ]:


plt.style.use('tableau-colorblind10')


# ## Carregando dataset

# In[ ]:


f = open('C:/Users/acer/Desktop/workspace/PYTHON/Recife/vacinados.csv', 'r', encoding="utf8")


# In[ ]:


data = f.read()


# In[ ]:


rows = data.split('\n')


# In[ ]:


print(rows)


# In[ ]:


full_data = []


# In[ ]:


for row in rows:
    split_row = row.split(";")
    full_data.append(split_row)


# In[ ]:


print(full_data)


# ## Contando as linhas do arquivo.

# In[ ]:


f = open('C:/Users/acer/Desktop/workspace/PYTHON/Recife/vacinados.csv', 'r', encoding="utf8")


# In[ ]:


data = f.read()


# In[ ]:


rows = data.split('\n')


# In[ ]:


full_data = []


# In[ ]:


for row in rows:
    split_row = row.split(";")
    full_data.append(split_row)


# In[ ]:


count = 0
for row in full_data:
    count += 1


# In[ ]:


print(count)


# ## Contando colunas do arquivo.

# In[ ]:


f = open('C:/Users/acer/Desktop/workspace/PYTHON/Recife/vacinados.csv', 'r', encoding="utf8")
data = f.read()
rows = data.split('\n')
full_data = []


# In[ ]:


for row in rows:
    split_row = row.split(";")
    full_data.append(split_row)
    first_row = full_data[0]
count = 0


# In[ ]:


for column in first_row:
    count = count + 1


# In[ ]:


print(count)


# ## Carregando arquivo com pandas

# In[88]:


import pandas as pd


# In[89]:


file1 = "C:/Users/acer/Desktop/workspace/PYTHON/Recife/vacinados.csv"


# In[90]:


df = pd.read_csv("vacinados.csv", engine="python", sep=';', quotechar='"', error_bad_lines=False)


# In[91]:


df.head()


# In[ ]:




