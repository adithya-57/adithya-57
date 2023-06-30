#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys
get_ipython().system('{sys.executable} -m pip install opencv-python')


# In[3]:


import cv2
image=cv2.imread("OIP.jpeg")


# In[5]:


g=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
i=cv2.bitwise_not(g)
b=cv2.GaussianBlur(i,(21,21),0)
o=cv2.bitwise_not(b)
s=cv2.divide(g,i,scale=256.0)
cv2.imwrite("lalgudi.png",s)


# In[ ]:




