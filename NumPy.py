#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
a=np.array([1,2,3,4,5], dtype=int)
print(a)


# In[17]:


b=np.array([[1,2,3,4,5],[5,6,7,8,9]])
print(b)


# In[18]:


# getting shape
b.shape


# In[11]:


# Getting type
a.dtype    # dtype is data type


# In[19]:


# Getting Dimension
b.ndim


# In[21]:


# Getting size
a.itemsize


# In[24]:


# Getting total size
b.nbytes   # size in bytes


# In[30]:


# Getting specific element [r,c]
a=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
a[1,2]                 # getting data from matrix 


# In[31]:


# Getting specific row
a[1,:]       # (1,:) all data from 1st row


# In[32]:


# Getting specific column
a[:,2]       # (:,1) all data from 1st column


# In[36]:


# getting more fancy (start inde: end index: step size)
a[1,1:5:2]      


# In[45]:


# Changing value from array
a[0,4]=999
print(a)


# In[47]:


# 3-D Array
x=np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])
print(x)


# In[50]:


# getting specific element
x[:,1,:]                


# In[56]:


# Replace
x[:,1,:]= [[111,222,333,444],[555,666,777,888]]
print(x)


# In[85]:


# all ones matrix
np.ones((2,3,4))


# In[159]:


np.ones((3,4))


# In[83]:


# all zeroes matrix
np.zeros((2,3))


# In[75]:


# any other no. in matrix form
np.full((2,3),111)


# In[81]:


# random decimal no.
np.random.rand(2,3)


# In[86]:


np.random.random_sample(x.shape)               # getting matrix size of x as a sample


# In[89]:


# Identity matrix
np.identity(4)


# 

# In[105]:


# Repeat an array
a=np.array([[1,2,3]])
r=np.repeat(a,3,axis=0)
print(r)


# In[106]:


a=np.array([1,2,3])
r=np.repeat(a,4,axis=0)
print(r)


# In[111]:


a=np.array([[1,2,3]])
r=np.repeat(a,3,axis=1)
print(r)


# In[108]:


a=np.array([[1,2,3]])
r=np.repeat(a,3)
print(r)


# In[117]:


################ ********* ###############
a=np.ones((5,5))
b=np.zeros((3,3))
b[1,1]=9
print(a)
print(b)


# In[119]:


a[1:4,1:4]=b
print(a)


# In[121]:


# Mathematics
a=np.array([2,3,4,5,6])
a+=2
print(a)


# In[123]:


a=np.array([2,3,4,5,6])
a-=2
print(a)


# In[125]:


a=np.array([2,3,4,5,6])
a*=2
print(a)


# In[129]:


a=np.array([2,3,4,5,6])
a=a/2
print(a)


# In[130]:


a=np.array([2,3,4,5,6])
a**=2
print(a)


# In[131]:


a=np.array([2,3,4,5,6])
a=np.sin(a)
print(a)


# In[132]:


a=np.array([2,3,4,5,6])
np.cos(a)


# In[134]:


# Linear Algebra
a=np.ones((2,3))
b=np.full((3,2),3)
print(a)
print(b)


# In[137]:


# for multipication of two matrix
np.matmul(a,b)          # matmul is matri multiplication


# In[140]:


# Finding Determinant
c=np.identity(4)
np.linalg.det(c)       # for finding the determinant


# In[142]:


# Statistics
stats=np.array([[1,2,3,4],[5,6,7,8]])
print(stats)


# In[143]:


np.min(stats)


# In[145]:


np.min(stats,axis=0)   # axis=0 for row


# In[146]:


np.min(stats,axis=1)    # axis=1 for column


# In[147]:


np.max(stats)


# In[148]:


np.max(stats,axis=0)


# In[149]:


np.max(stats,axis=1)


# In[150]:


np.sum(stats)


# In[151]:


np.sum(stats,axis=1)


# In[152]:


np.sum(stats,axis=0)


# In[153]:


# Vertical stacking vectors
v1=np.array([1,2,3,4])
v2=np.array([5,6,7,8])              # stack or vstack are same and used for vertical stacking
V=np.vstack([v1,v2])
print(V)


# In[154]:


V=np.vstack([v1,v2,v2])
print(V)


# In[157]:


V=np.vstack([v1,v1,v1,v2,v2])
print(V)


# In[158]:


# Horizontal stacking vectors
h1=np.array([1,2,3,4])
h2=np.array([5,6,7,8])
H=np.hstack([h1,h2])
print(H)


# In[59]:


import numpy as np
a=np.array([[1,2],[4,5]])
b=np.array([[11,12],[23,45]])
x=np.linalg.inv(a).dot(b)
x


# In[60]:


a.T


# In[90]:


np.random.randint(9, size=(4, 4))


# In[97]:


import pandas as pd
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 10)
a=pd.read_excel("C:\\Users\\ANKIT\\Desktop\\Excel_DATA.xlsx",sheet_name="Data",skiprows=1)
a


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




