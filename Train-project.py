#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv("D:/Datasets/train (1).csv")


# In[3]:


df.head()


# In[4]:


df.info()


# In[5]:


import seaborn as sns


# In[6]:


_=sns.distplot(df["SalePrice"])


# In[7]:


total=df.isnull().sum().sort_values(ascending=False)


# In[8]:


total


# In[9]:


percent=df.isnull().sum()/df.shape[0]


# In[10]:


missing_data=pd.concat([total,percent],axis=1,keys=["Total","Percent"])


# In[11]:


missing_data.head(20).sort_index()


# In[12]:


null_has_meaning=["Alley","BsmtCond","BsmtExposure","BsmtFinType1","BsmtFinType2",
                 "BsmtQual","Fence","FireplaceQu","GarageCond","GarageFinish","GarageQual","GarageType","PoolQC","MiscFeature"]


# In[13]:


for i in null_has_meaning:
    df[i].fillna("None",inplace=True)
    


# In[14]:


total=df.isnull().sum().sort_values(ascending=False)
percent=df.isnull().sum()/df.shape[0]
missing_data=pd.concat([total,percent],axis=1,keys=["Total","Percent"])
missing_data.head(20)


# In[15]:


df.drop("LotFrontage",axis=1,inplace=True)


# In[16]:


df.dtypes


# In[17]:


import matplotlib.pyplot as plt


# In[18]:


var="GarageYrBlt"
data=pd.concat([df["SalePrice"],df[var]],axis=1)
f,ax=plt.subplots(figsize=(8,6))
fig=sns.boxplot(x=var,y="SalePrice",data=data)
fig.axis(ymin=0,ymax=800000)
plt.xticks(rotation=90)


# In[19]:


total=df.isnull().sum().sort_values(ascending=False)
percent=df.isnull().sum()/df.shape[0]
missing_data=pd.concat([total,percent],axis=1,keys=["Total","Percent"])
missing_data.head(20)


# In[20]:


df["GarageYrBlt"].fillna(df["GarageYrBlt"].median(),inplace=True)
df["MasVnrArea"].fillna(df["MasVnrArea"].median(),inplace=True)
df["MasVnrType"].fillna("None",inplace=True)


# In[21]:


total=df.isnull().sum().sort_values(ascending=False)
percent=df.isnull().sum()/df.shape[0]
missing_data=pd.concat([total,percent],axis=1,keys=["Total","Percent"])
missing_data.head(20)


# In[22]:


df.dropna(inplace=True)


# In[23]:


total=df.isnull().sum().sort_values(ascending=False)
percent=df.isnull().sum()/df.shape[0]
missing_data=pd.concat([total,percent],axis=1,keys=["Total","Percent"])
missing_data.head(20)


# In[24]:


types_train=df.dtypes
num_train=types_train[(types_train=="int64") | (types_train==float)]


# In[25]:


cat_train=types_train[(types_train==object)]


# In[26]:


pd.DataFrame(types_train)[0].value_counts()


# In[27]:


num_train


# In[28]:


numerical_values_train=list(num_train.index)


# In[29]:


num_train


# In[30]:


numerical_values_train


# In[31]:


categorical_values_train=list(cat_train.index)
categorical_values_train


# In[32]:


sns.distplot(df["SalePrice"])


# In[33]:


import numpy as np


# In[34]:


sns.distplot(np.log(df["SalePrice"]))


# In[35]:


df["TransformedPrice"]=np.log(df["SalePrice"])


# In[36]:


categorical_values_train


# In[37]:


df["MSZoning"].value_counts()


# In[38]:


df[categorical_values_train]


# In[39]:


set(df["MSZoning"])


# In[40]:


for i in categorical_values_train:
    feature_set=set(df[i])
    for j in feature_set:
        feature_list=list(feature_set)
        df.loc[df[i]==j,i]=feature_list.index(j)
        


# In[41]:


df.head()


# In[42]:


X=df.drop(["Id","SalePrice","TransformedPrice"],axis=1)


# In[43]:


y=df["TransformedPrice"]


# In[44]:


from sklearn.model_selection import train_test_split


# In[45]:


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=100)


# In[46]:


params={"alpha":[0.0001,0.001,0.01,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,2,3,4,5,6,7,8,9,10,20,50,100,500,1000]}


# In[47]:


from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.model_selection import GridSearchCV


# In[49]:


lasso=Lasso()
folds=5
model_cv=GridSearchCV(estimator=lasso,
                     param_grid=params,scoring="neg_mean_absolute_error",
                      return_train_score=True,
                     cv=folds,verbose=1)
model_cv.fit(X_train,y_train)


# In[50]:


cv_results=pd.DataFrame(model_cv.cv_results_)


# In[51]:


cv_results["param_alpha"]=cv_results["param_alpha"].astype("float32")


# In[52]:


cv_results.dtypes


# In[54]:


plt.plot(cv_results["param_alpha"],cv_results["mean_train_score"])
plt.plot(cv_results["param_alpha"],cv_results["mean_test_score"])
plt.xlabel("alpha")
plt.ylabel("Negative Mean Absolute Error")
plt.legend(["train_score","test_score"],loc="upper left")
plt.show()


# In[55]:


alpha=50
lasso=Lasso(alpha=alpha)
lasso.fit(X_train,y_train)


# In[56]:


lasso.coef_


# In[57]:


ridge=Ridge()
folds=5
model_cv=GridSearchCV(estimator=ridge,
                     param_grid=params,scoring="neg_mean_absolute_error",
                      return_train_score=True,
                     cv=folds,verbose=1)
model_cv.fit(X_train,y_train)


# In[58]:


cv_results=pd.DataFrame(model_cv.cv_results_)


# In[60]:


cv_results.dtypes


# In[61]:


cv_results["param_alpha"]=cv_results["param_alpha"].astype("float32")


# In[62]:


plt.plot(cv_results["param_alpha"],cv_results["mean_train_score"])
plt.plot(cv_results["param_alpha"],cv_results["mean_test_score"])
plt.xlabel("alpha")
plt.ylabel("Negative Mean Absolute Error")
plt.legend(["train_score","test_score"],loc="upper left")
plt.show()


# In[63]:


alpha=10
ridge=Ridge(alpha=alpha)
ridge.fit(X_train,y_train)


# In[64]:


ridge.coef_


# In[ ]:




