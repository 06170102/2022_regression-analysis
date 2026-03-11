#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np


# In[2]:


df = pd.read_csv('NCHS_-_Death_rates_and_life_expectancy_at_birth.csv') #讀入資料


# In[3]:


df.head() #有空值，需要清除


# In[4]:


df.count() #少了9筆


# In[5]:


df = df.dropna(axis=0) #刪除有缺失的row


# In[6]:


df.count()


# 1. Suppose you want to test whether women have longer life expectancy than men. How would you do the inference?

# 將題目要證實的資訊放在 h1 
# ho:u女性平均壽命 <=u男性平均壽命 
# VS
# h1:u女性平均壽命 >u男性平均壽命 
# 
# 
# 假設兩母體在相互獨立且符合常態下，在母體變異數未知的情況下，樣本數 大於 30 可用S^2 估計母體變異數，以此進行Z_test右尾檢定 來檢定顯著性。(假設 alpha=0.05)。

# In[7]:


man = df[df['Sex']=='Male'] #選定男性資料


# In[8]:


Woman = df[df['Sex']=='Female'] #選定女性資料


# In[9]:


man = list(man['Average Life Expectancy (Years)']) #取出男性平均壽命資料


# In[10]:


woman =list(Woman['Average Life Expectancy (Years)']) #取出女性平均壽命資料


# In[11]:


from statsmodels.stats.weightstats import ztest as ztest


# In[12]:


ztest(woman, man, value=0)  #檢定統計量Ｚ ＝ 5.88 > Z_0.05 =1.68 reject h0


# 結論:檢定統計量 Z=5.88 > Z_0.05 = 1.68 ，拒絕虛無假設 h0，女性平均壽命大於男性。

# 

# 2. Suppose you want to test whether race makes any difference on life expectancy. How would you do the inference?

# 假設
# 
# ho:黑人平均壽命 == 白人平均壽命 
# VS
# h1:黑人平均壽命 != 白人平均壽命 
# 
# 
# 假設兩母體在相互獨立且符合常態下，在母體變異數未知的情況下，樣本數 大於 30 可用S^2 估計母體變異數，以此進行Z_test雙尾檢定 來檢定顯著性。(假設 alpha=0.05)。

# In[14]:


b = df[df['Race']=='Black'] #選定黑人資料
w = df[df['Race']=='White'] #選定白人資料


# In[15]:


b = list(b['Average Life Expectancy (Years)'])  #取出黑人平均壽命資料
w = list(w['Average Life Expectancy (Years)'])  #取出白人平均壽命資料


# In[16]:


ztest(b, w, value=0)  #檢定統計量Ｚ ＝ -10.18 reject h0


# 結論:檢定統計量 Z＝ -10.18 ，拒絕虛無假設 h0，黑人平均壽命不等於白人。種族不同確實造成不同的平均壽命。

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




