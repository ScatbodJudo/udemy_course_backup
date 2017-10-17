"""
This code is making over 21 billion comparisons...
it needs a progress bar.

see the article here:
https://stackoverflow.com/questions/18603270/progress-indicator-during-pandas-operations-python
"""
# coding: utf-8

# In[3]:


import os
import pandas
from difflib import SequenceMatcher
from difflib import get_close_matches
os.listdir()


# In[4]:


df200 = pandas.read_csv('200NumberEmails.csv')


# In[7]:


df900 = pandas.read_csv('900NumberEmails.csv', encoding = 'latin1')


# In[10]:


df200 = df200.set_index('Constituent ID')
df900 = df900.set_index('Constituent ID')


# In[14]:


df200_shape = df200.shape
df900_shape = df900.shape


# In[16]:


print(df200_shape[0]*df200_shape[1])


# In[17]:


print(df900_shape[0]*df900_shape[1])


# In[18]:


print('total: '+str(58955*361210))


# In[ ]:


n=0
for row200 in df200.itertuples():
    for i in row200:
        for row900 in df900.itertuples():
            for j in row900:
                if i==j:
                    n = n+1
print(n)                   
                    


# In[48]:


