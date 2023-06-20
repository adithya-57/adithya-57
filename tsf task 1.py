#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
url="http://bit.ly/w-data"
s=pd.read_csv(url)
s.head()


# In[13]:


s.head(8)


# In[18]:


x=s.iloc[:,:-1].values
y=s.iloc[:,-1].values


# In[19]:


from sklearn.model_selection import train_test_split
gt,gte,rt,rte=train_test_split(x,y,test_size=0.35,random_state=2)


# In[20]:


from sklearn.linear_model import LinearRegression
m=LinearRegression()
v=m.fit(gt,rt)
v


# In[54]:


o=m.predict(gte)
o


# In[22]:


from sklearn.metrics import mean_absolute_error
dp=mean_absolute_error(rte,o)
dp


# In[29]:


h=s['Hours']
i=s['Scores']
sns.distplot(h)
sns.distplot(i)


# In[32]:


p=v.coef_
q=v.intercept_
l=p*x+q
plt.scatter(x,y)
plt.plot(x,l)
plt.show()


# In[33]:


sns.scatterplot(x='Hours',y='Scores',data=s)
plt.title("relation btwn hours and distances")
plt.show()


# In[39]:


print("score of a student will be",m.predict([[9.6]]))


# In[41]:


plt.scatter(x=gte,y=rte,color='blue')
plt.plot(gte,m.predict(gte),color='brown')
plt.xlabel("hours")
plt.ylabel("scores")
plt.show()


# In[ ]:




