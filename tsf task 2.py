#!/usr/bin/env python
# coding: utf-8

# In[16]:


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
z=pd.read_csv("Iris.csv")
p=z.head(60)
p


# In[17]:


t=p.drop(['Id','SepalWidthCm','SepalLengthCm'],axis=1)
t


# In[20]:


f=t.replace({'Species':{'Iris-setosa':1,'Iris-versicolor':2}})
f


# In[29]:


k=f.drop(['PetalWidthCm','PetalLengthCm'],axis=1)
k


# In[30]:


from sklearn.model_selection import train_test_split
gt,gte,rt,rte=train_test_split(f,k,test_size=0.35,random_state=2)


# In[50]:


from sklearn.neighbors import KNeighborsClassifier
m=KNeighborsClassifier(n_neighbors=2,metric='minkowski',p=2)
v=m.fit(gt,rt)
v


# In[51]:


y=m.predict(gt)
y


# In[57]:


h=m.predict(gte)
h


# In[43]:


plt.scatter(x="SepalWidthCm",y="SepalLengthCm",data=p)
plt.title("flower classification")
plt.show()


# In[59]:



plt.plot(v.predict(gte),color='brown')
plt.xlabel("Sepal length")
plt.ylabel("Sepal Width")
plt.show()


# In[ ]:




