#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 라이브러리 불러오기
import pandas as pd
import numpy as np
np.set_printoptions(precision=4, suppress=True)
import matplotlib.pyplot as plt
import seaborn as sns


# In[6]:


file_path ='E:\(세미2)breastcancerdb\data\BREAST1.csv'
file_path


# In[9]:


df= pd.read_csv(file_path)
df.head()


# In[ ]:




