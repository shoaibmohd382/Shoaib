#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


gdp_current_price=pd.read_csv("Gross Domestic Product (GDP) at Current Price.csv")


# In[3]:


gdp_current_price


# In[4]:


pd.pivot_table(gdp_current_price,index=['Items Description','Duration'])


# In[5]:


gdp_current_price


# In[6]:


gdp_current_price=gdp_current_price.drop(gdp_current_price.index[[3,9]])


# In[7]:


gdp_current_price.info()


# In[8]:


#index_to_drop=gdp_current_price.index[((gdp_current_price["Items Description"]=='(% Growth over previous year)') 
              #           & (gdp_current_price["Duration"]=="2016-17"))]


# In[9]:


#gdp_current_price.drop(index_to_drop)


# In[10]:


gdp_current_price


# In[11]:


column_attributes=list(gdp_current_price.columns)


# In[12]:


del(column_attributes[0])


# In[13]:


del(column_attributes[0])


# In[14]:


states=column_attributes


# In[15]:


states


# In[16]:


state_mean={}
for column in gdp_current_price:
    if column in states:
        mean=gdp_current_price[gdp_current_price["Items Description"]=="(% Growth over previous year)"][column].mean()
        state_mean[column]=mean
state_mean["Items Description"]="Average growth rate"
gdp_current_price=gdp_current_price.append(state_mean,ignore_index=True)


# In[17]:


gdp_current_price


# In[18]:


gdp_current_price=gdp_current_price.iloc[[2,7,8],:]


# In[19]:


gdp_current_price


# In[20]:


gdp=gdp_current_price.T


# In[21]:


gdp


# In[22]:


gdp.columns=gdp.iloc[0]


# In[23]:


gdp=gdp[1:]


# In[24]:


gdp=gdp[1:]


# In[25]:


gdp


# In[26]:


gdp["Average growth rate"].sort_values().plot.bar()


# 1. Rate of GDP Growth in North East States like mizoram, Tripura and Nagaland is high.
# 2. States like goa, Meghalaya, Odisha, sikkim and J&K is struggling with GDP growth
# 3. All India GDP is not so relatively low
# 4. GDP growth of bihar, chattisgarh, A&N, Andhra Pradesh, Karnataka and Arunachal Pradesh are relatively high
# 5. For all other states, GDP growth is medium

# In[27]:


gdp["GSDP - CURRENT PRICES (` in Crore)"].drop("All_India GDP",axis=0).sort_values().plot.bar()


# In[28]:


states


# # Part 1-B

# In[29]:


states=['Andhra_Pradesh',
 'Arunachal_Pradesh',
 'Assam',
 'Bihar',
 'Chhattisgarh',
 'Goa',
 'Gujarat',
 'Haryana',
 'Himachal_Pradesh',
 'Jammu & Kashmir',
 'Jharkhand',
 'Karnataka',
 'Kerala',
 'Madhya_Pradesh',
 'Maharashtra',
 'Manipur',
 'Meghalaya',
 'Mizoram',
 'Nagaland',
 'Odisha',
 'Punjab',
 'Rajasthan',
 'Sikkim',
 'Tamil Nadu',
 'Telangana',
 'Tripura',
 'Uttar_Pradesh',
 'Uttarakhand',
 'West Bengal']


# In[30]:


import os


# In[31]:


gsva=pd.DataFrame()


# In[32]:


path=("C:\\Users\\Lenovo\\GSVA\\")


# In[33]:


listOfFiles=os.listdir(path)


# In[34]:


len(listOfFiles)


# In[35]:


len(states)


# In[36]:


for filename in listOfFiles:
    for statename in states:
        if statename in filename:
            filepath=path+filename
            data=pd.read_csv(filepath,encoding="ISO-8859-1")
            data=data[['Item','2014-15']]
            data=data.T
            data.columns=data.iloc[0]
            data=data[1:]
            data["state"]=statename
            gsva=pd.concat([data,gsva])
                
            
            


# In[37]:


gsva.set_index("state",inplace=True)


# In[38]:


gsva


# In[39]:


gsva.columns


# In[40]:


gsva["Per Capita GSDP (Rs.)"].sort_values().plot.bar()


# In[41]:


gsva["Per Capita GSDP (Rs.)"].sort_values()["Goa"]/gsva["Per Capita GSDP (Rs.)"].sort_values()["Bihar"]


# In[42]:


gsva.columns


# In[43]:


gsva


# In[44]:


gsva["primary_gdp_percent"]=0
gsva["secondary_gdp_percent"]=0
gsva["tertiary_gdp_percent"]=0


# In[45]:


gsva


# In[46]:


list(gsva.columns).index("Tertiary")


# In[47]:


for i in range(len(gsva)):
    gsva.iloc[i,37]=gsva.iloc[i,6]/gsva.iloc[i,30]
    gsva.iloc[i,38]=gsva.iloc[i,10]/gsva.iloc[i,30]
    gsva.iloc[i,39]=gsva.iloc[i,26]/gsva.iloc[i,30]


# In[48]:


gsva.sort_values("Per Capita GSDP (Rs.)")[["primary_gdp_percent","secondary_gdp_percent","tertiary_gdp_percent"]].plot(kind="bar",stacked=True)


# In[49]:


gsva.sort_values("Per Capita GSDP (Rs.)")["Population ('00)"].plot(kind="bar")


# 1. For states which has low per capita income, has significant dependence on primary source whereas states which have high per capta income relies more on secondary and tertiary
# 2.UP has high GDP but due to its population, has low per capita income
# 

# In[50]:


per_capita=gsva["Per Capita GSDP (Rs.)"].sort_values()


# In[51]:


per_capita.quantile([0.20,0.5,0.8,1])


# In[52]:


per_capita.sort_values(ascending=False)


# In[79]:



category_1 = ['Goa', 'Sikkim', 'Kerala', 'Haryana']
category_2 = ['Arunachal_Pradesh', 'Punjab','Telangana', 'Gujarat', 'Karnataka', 
       'Maharashtra', 'Uttarakhand']
category_3 = [ 'Madhya_Pradesh', 'Odisha', 'Meghalaya', 'Tripura', 'Rajasthan',
       'Chhattisgarh', 'Nagaland', 'Andhra_Pradesh']
category_4 = ['Bihar', 'Uttar_Pradesh', 'Manipur', 'Assam', 'Jharkhand' ]

categories_columns = ['Agriculture, forestry and fishing', 'Mining and quarrying', 'Manufacturing',
                      'Electricity, gas, water supply & other utility services', 'Construction',
                      'Trade, repair, hotels and restaurants',
                      'Transport, storage, communication & services related to broadcasting', 
                      'Financial services', 'Real estate, ownership of dwelling & professional services',
                      'Public administration', 'Other services', 'Taxes on Products', 'Subsidies on products']


# In[54]:


gsva


# # Category 1

# In[72]:


agg=gsva.loc[category_1,categories_columns].sum()


# In[73]:


agg_gsdp=gsva.loc[category_1,"Gross State Domestic Product"].sum()


# In[74]:


agg


# In[75]:


agg_gsdp


# In[82]:


round(100*agg/agg_gsdp).sort_values(ascending=False)


# In[76]:


round(100*agg/agg_gsdp).sort_values(ascending=False)[0:6].plot.bar()


# Category 1: There are only 4 states in this category, all of which are small (area-wise) and have good industrial base , agricultural, trade and real estate. 
# 1. Trade and hospitality bisiness should be promoted further
# 2. Manufacturing should be further promoted

# # Category 2 States

# In[78]:


agg=gsva.loc[category_2,categories_columns].sum()
agg_gsdp=gsva.loc[category_2,"Gross State Domestic Product"].sum()
round(100*agg/agg_gsdp).sort_values(ascending=False)[0:6].plot.bar()


# 1. These states have relatively good per capita gdp and are drivcen by around equal percentage by industries and agriclture. These implies that these states have pool of talent to drive industries and agriculture. Because of the talent, other industries can take their advantage and set up good industries.
# 2. States like karnataka, tamil nadu , gujarat and maharashtra, which has huge coastal area can setup ports. Coastal area can help in harness clean energy and fisheries can be increased. Similarly, tourism industry should also be encouraged.

# # Category 3 States

# In[80]:


agg=gsva.loc[category_3,categories_columns].sum()
agg_gsdp=gsva.loc[category_3,"Gross State Domestic Product"].sum()
round(100*agg/agg_gsdp).sort_values(ascending=False)[0:6].plot.bar()


# # Category 4 States

# In[81]:


agg=gsva.loc[category_4,categories_columns].sum()
agg_gsdp=gsva.loc[category_4,"Gross State Domestic Product"].sum()
round(100*agg/agg_gsdp).sort_values(ascending=False)[0:6].plot.bar()


# # Part 2

# In[97]:


drop_out_rate=pd.read_csv("rs_session243_au570_1.1.csv",index_col=0)


# In[98]:


drop_out_rate


# In[99]:


drop_out_rate.rename(columns={'Level of Education - State':'State'},inplace=True)


# In[101]:


drop_out_rate.replace({"Andhra Pradesh":"Andhra_Pradesh","Arunachal Pradesh":"Arunachal_Pradesh",
                      "Uttar Pradesh":"Uttar_Pradesh","Madhya Pradesh":"Madhya_Pradesh"},inplace=True)


# In[102]:


drop_out_rate


# In[ ]:





# In[ ]:





# In[103]:


drop_out_rate=drop_out_rate.set_index("State")


# In[104]:


drop_out_rate


# In[106]:


gsva_drop=pd.merge(gsva,drop_out_rate,how="inner",left_index=True,right_index=True)


# In[108]:


gsva_drop.columns


# In[110]:


gsva_primary=gsva_drop[["Per Capita GSDP (Rs.)","Primary - 2014-2015"]]


# In[114]:


gsva_primary.dropna(inplace=True)


# In[117]:


gsva_primary['Primary - 2014-2015']=gsva_primary['Primary - 2014-2015'].astype(int)


# In[121]:


import matplotlib.pyplot as plt


# In[124]:


gsva_primary.plot.scatter(x="Per Capita GSDP (Rs.)",y="Primary - 2014-2015")


# In[125]:


gsva_secondary=gsva_drop[["Per Capita GSDP (Rs.)","Secondary - 2014-2015"]]
gsva_secondary.dropna(inplace=True)
gsva_secondary['Secondary - 2014-2015']=gsva_secondary['Secondary - 2014-2015'].astype(int)
gsva_secondary.plot.scatter(x="Per Capita GSDP (Rs.)",y="Secondary - 2014-2015")


# In[ ]:




