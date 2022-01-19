#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv(r"C:/Users/tanvi/Downloads/archive/covid_19_india.csv")


# In[6]:


data.head()


# In[8]:


data.columns


# In[10]:


data.tail()


# In[12]:


data.describe()


# In[14]:


data.isnull().sum()


# # Relating variables with the help of different plots

# In[21]:


sns.relplot(x="Cured" , y="Deaths" ,  data=data)


# In[23]:


sns.relplot(x="Cured" , y="Deaths" , hue="Confirmed" , data=data)


# In[25]:


sns.pairplot(data)


# In[29]:


sns.relplot(x='Cured' , y='Deaths' , kind='line' , data=data)


# In[ ]:





# In[ ]:




