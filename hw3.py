#!/usr/bin/env python
# coding: utf-8

# In[1]:


#匯入資料
import pandas as pd

dta = pd.read_stata('crime.dta')
dta = dta.applymap(lambda x: str(x).encode('latin-1').decode('utf-8'))


# In[2]:


dta #資料共51筆觀察值，9個col


# In[3]:


dta = dta.drop(['state'],axis =1)
dta = dta.astype(float) #將數值行資料，轉為float
dta.describe() #check data 統計資訊


# In[ ]:





# In[4]:


dta = dta[['crime','poverty']] #選取題目要求的columns


# In[ ]:





# In[5]:


dta.describe() 


# In[6]:


#1. Do a simple linear regression with crime against poverty. Draw the data and your regression line.


# In[7]:


#首先根據題目，x='poverty', y='crime'。繪製散佈圖。我們可看出在poverty大的情況下，點的分佈非常離散，有離群值出現。
ax = dta.plot(x='poverty', y='crime', kind='scatter')


# In[8]:


#接著，用ＯＬＳ法建立迴歸model。


# In[9]:


import statsmodels.api as sm
import numpy as np

model = sm.OLS(dta.crime, sm.add_constant(dta.poverty))
p = model.fit()

print(p.summary())
#根據OLS法，估出迴歸係數。 bo_hat = -86.20 b1_hat = 49.02。 adjusted r2 = 0.244


# In[ ]:





# In[10]:


#繪製散佈圖 和 ols regression line
t = model.fit().params #get parameters
x = np.arange(5, 30)
ax = dta.plot(x='poverty', y='crime', kind='scatter')
ax.plot(x, t.const + t.poverty * x) #plot ols line


# In[ ]:





# In[12]:


#2 =======================================================
#Repeat 1, but using least absolute value (aka least absolute deviation) instead of least square. Draw the data and your regression line, and compare with the result in 1


# In[13]:


import statsmodels.formula.api as smf
import matplotlib.pyplot as plt


# In[14]:


# OLS = argmin(sum (yi - f(xi))**2) #差距採用距離的平方。最小化以估出回歸線。efficienct
# LAD = argmin(sum |yi - f(xi)|)   ＃差距採用距離的絕對值。 robust


# In[15]:


#這邊使用quantaile regression model 來估回歸線。在q=0.5的情況下為special case，會跟ＬＡＤ公式一致。
mod = smf.quantreg("crime ~ poverty", dta)
res = mod.fit(q=0.5)
print(res.summary())


# In[16]:


#根據LAD法，估出迴歸係數。 bo_hat = -28.77 b1_hat = 41.02。 斜率較ＯＬＳ法小，受離群值影響較小。


# In[17]:


p = mod.fit().params


# In[18]:


p


# In[19]:


#將結果畫在同張圖上比較。紅線為OLS迴歸線，藍線為LAD迴歸線。可看出ols受離群值影響，導致線被往上拉升，較為陡。
#而LAD為受影響較小。
x = np.arange(5, 30)


ax = dta.plot(x='poverty', y='crime', kind='scatter')


ax.plot(x, p.Intercept + p.poverty * x) # LAD line
ax.plot(x, t.const + t.poverty * x,color = 'r') #ols line


# In[ ]:





# In[ ]:





# In[ ]:




