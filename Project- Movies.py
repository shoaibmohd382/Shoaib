#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt


# In[13]:


Movies= pd.read_csv("C:/Users/MOHD.SHOAIB/Desktop/SHOAIB/DEEP MACHINE LEARNING WITH PYTHON/CASE STUDY 1/Movie+Assignment+Data.csv")


# In[14]:


Movies.head()


# In[15]:


Movies.shape


# In[16]:


Movies.describe


# In[17]:


Movies.info


# In[18]:


Movies["budget"]=Movies["budget"]/1000000


# In[19]:


Movies.head()


# In[20]:


Movies["Gross"]=Movies["Gross"]/1000000


# In[21]:


Movies.head()


# In[22]:


Movies["Profit"]=Movies["Gross"]-Movies["budget"]


# In[23]:


Movies.head()


# In[24]:


Movies.sort_values(by="Profit",ascending=False)


# In[25]:


Movies.iloc[:10,:]


# In[26]:


sns.jointplot("budget","Profit",Movies)
plt.show()


# In[27]:


Movies.head()


# In[28]:


Movies[Movies["Profit"]<0]


# In[29]:


Movies["MetaCritic"]= Movies["MetaCritic"]/10


# In[30]:


Movies.head()


# In[31]:


Movies["Avg_rating"]=(Movies["IMDb_rating"]+Movies["MetaCritic"])/2


# In[32]:


Movies.head()


# In[33]:


Movies.sort_values(by="Avg_rating",ascending=False)


# In[34]:


Movies[["Title","IMDb_rating","MetaCritic","Avg_rating"]]
[abs(Movies["IMDb_rating"]-Movies["MetaCritic"]<0.5)]
Movies.loc[abs(Movies["IMDb_rating"]-Movies["MetaCritic"]<0.5)]
Movies.sort_values(by="Avg_rating",ascending=False)


# In[ ]:





# In[35]:


Movies["Avg_rating"]>8


# In[36]:


Movies.loc[Movies["Avg_rating"]>8]


# In[37]:


Movies1=Movies[["Title","IMDb_rating","MetaCritic","Avg_rating"]]
[abs(Movies1["IMDb_rating"]-Movies1["MetaCritic"]<0.5)]
Movies1.loc[abs(Movies["IMDb_rating"]-Movies1["MetaCritic"]<0.5)]
Movies1.sort_values(by="Avg_rating",ascending=False)


# In[38]:


[abs(Movies1["IMDb_rating"]-Movies1["MetaCritic"]<0.5)]
Movies1.loc[abs(Movies1["IMDb_rating"]-Movies1["MetaCritic"]<0.5)]
Movies1.sort_values(by="Avg_rating",ascending=False)


# In[39]:


Movies1.loc[Movies1["Avg_rating"]>8]


# In[40]:


Movies1=Movies1.sort_values(by="Avg_rating",ascending=False)
UniversalAcclaim=Movies1.loc[Movies1["Avg_rating"]>=8]
UniversalAcclaim


# In[41]:


Group=Movies.pivot_table(values=["actor_1_facebook_likes","actor_2_facebook_likes","actor_3_facebook_likes"],
                   aggfunc="sum",index=["actor_1_name","actor_2_name","actor_3_name"])


# In[42]:


Group["Total_likes"]=Group["actor_1_facebook_likes"]+Group["actor_2_facebook_likes"]+Group["actor_3_facebook_likes"]


# In[43]:


Group.sort_values(by="Total_likes",ascending=False,inplace=True)


# In[44]:


Group


# In[45]:


Group.reset_index(inplace=True)


# In[46]:


Group


# In[47]:


Group.iloc[0:5,:]


# In[48]:


import matplotlib.pyplot as plt


# In[49]:


plt.hist(Group["Total_likes"])
plt.show()


# In[51]:


fig,ax=plt.subplots()
ax.plot(Group["actor_1_name"],Group["actor_1_facebook_likes"])
plt.show


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[54]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




