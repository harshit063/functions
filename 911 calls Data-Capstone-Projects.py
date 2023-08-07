#!/usr/bin/env python
# coding: utf-8

# # 911 Calls Capstone Project

# For this capstone project i have choose the data of  911 call data from [Kaggle](https://www.kaggle.com/mchirico/montcoalert). The data contains the following fields:
# 
# * lat : String variable, Latitude
# * lng: String variable, Longitude
# * desc: String variable, Description of the Emergency Call
# * zip: String variable, Zipcode
# * title: String variable, Title
# * timeStamp: String variable, YYYY-MM-DD HH:MM:SS
# * twp: String variable, Township
# * addr: String variable, Address
# * e: String variable, Dummy variable (always 1)
# 

# ## Data and Setup

# In[1]:


import numpy as np 
import pandas as pd


# In[4]:


import matplotlib.pyplot as plt 
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


df = pd.read_csv('911.csv')


# In[6]:


df.info()


# In[7]:


df.head()


# top 5 zipcodes for 911 calls

# In[8]:


df['zip'].value_counts().head(5)


# **  the top 5 townships (twp) for 911 calls **

# In[16]:


df['twp'].value_counts().head(5)


# ** Take a look at the 'title' column, how many unique title codes are there? **

# In[14]:


df['title'].nunique()


# In[18]:


x = df['title'].iloc[0]


# In[20]:


x.split(':')[0]


# In[21]:


df['reason']=df['title'].apply(lambda title : title.split(':')[0])


# In[22]:


df['reason']


# ** What is the most common Reason for a 911 call based off of this new column? **

# In[24]:


df['reason'].value_counts()


# **  seaborn to create a countplot of 911 calls by Reason. **

# In[26]:


sns.countplot(x='reason',data=df)


# ___
# **  focusing on time information. What is the data type of the objects in the timeStamp column? **

# In[29]:


type(df['timeStamp'].iloc[0])


# ** You should have seen that these timestamps are still strings. Use [pd.to_datetime](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.to_datetime.html) to convert the column from strings to DateTime objects. **

# In[32]:


df['timeStamp']= pd.to_datetime(df['timeStamp'])


# In[33]:


type(df['timeStamp'].iloc[0])


# ** specific attributes from a Datetime object by calling them
# 
#     time = df['timeStamp'].iloc[0]
#     time.hour
# 
# **Using Jupyter's tab method to explore the various attributes you can call. Now that the timestamp column are actually DateTime objects, use .apply() to create 3 new columns called Hour, Month, and Day of Week. You will create these columns based off of the timeStamp column, reference the solutions if you get stuck on this step.**

# In[34]:


time = df['timeStamp'].iloc[0]
time.hour


# In[37]:


time.month


# In[39]:


df['Hour']=df['timeStamp'].apply(lambda time : time.hour)


# ** Notice how the Day of Week is an integer 0-6. Use the .map() with this dictionary to map the actual string names to the day of the week: **
# 
#     dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}

# In[40]:


df['Hour']


# In[49]:


df['Month']=df['timeStamp'].apply(lambda time : time.month)
df['DayOfWeek']=df['timeStamp'].apply(lambda time : time.dayofweek)


# In[50]:


df.head()


# In[52]:


dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}


# In[56]:


df['DayOfWeek']=df['DayOfWeek'].map(dmap)


# In[57]:


df.head()


# ** Now using seaborn to create a countplot of the Day of Week column with the hue based off of the Reason column. **

# In[63]:


sns.countplot(x='DayOfWeek',data=df,palette='viridis',hue='reason')
#for legend
plt.legend(bbox_to_anchor=(1.05,1),loc=2,borderaxespad=0)


# ** same for Month:**

# In[64]:


sns.countplot(x='Month',data=df,palette='viridis',hue='reason')
#for legend
plt.legend(bbox_to_anchor=(1.05,1),loc=2,borderaxespad=0)


# **Did you notice something strange about the Plot?**
# 
# _____
# 
# ** You should have noticed it was missing some Months, let's see if we can maybe fill in this information by plotting the information in another way, possibly a simple line plot that fills in the missing months, in order to do this, we'll need to do some work with pandas... **

# ** Now create a gropuby object called byMonth, where you group the DataFrame by the month column and use the count() method for aggregation. Use the head() method on this returned DataFrame. **

# In[169]:





# ** Now create a simple plot off of the dataframe indicating the count of calls per month. **

# In[175]:





# ** Now see if you can use seaborn's lmplot() to create a linear fit on the number of calls per month. Keep in mind you may need to reset the index to a column. **

# In[187]:





# **Create a new column called 'Date' that contains the date from the timeStamp column. You'll need to use apply along with the .date() method. ** 

# In[193]:





# ** Now groupby this Date column with the count() aggregate and create a plot of counts of 911 calls.**

# In[197]:





# ** Now recreate this plot but create 3 separate plots with each plot representing a Reason for the 911 call**

# In[199]:





# In[201]:





# In[202]:





# ____
# ** Now let's move on to creating  heatmaps with seaborn and our data. We'll first need to restructure the dataframe so that the columns become the Hours and the Index becomes the Day of the Week. There are lots of ways to do this, but I would recommend trying to combine groupby with an [unstack](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.unstack.html) method. Reference the solutions if you get stuck on this!**

# In[203]:





# ** Now create a HeatMap using this new DataFrame. **

# In[204]:





# ** Now create a clustermap using this DataFrame. **

# In[205]:





# ** Now repeat these same plots and operations, for a DataFrame that shows the Month as the column. **

# In[207]:





# In[208]:





# In[209]:





# **Continue exploring the Data however you see fit!**
# # Great Job!
