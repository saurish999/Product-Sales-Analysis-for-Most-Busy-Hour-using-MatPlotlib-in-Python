#!/usr/bin/env python
# coding: utf-8

# In[25]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[6]:


Order_Details = pd.read_csv("Order_Details.csv")


# In[7]:


Order_Details


# In[10]:


## Creating separate Time column for date in YY-MM-DD and time in HH:MM:SS format
Order_Details['Time'] = pd.to_datetime(Order_Details['Transaction Date']) 

## Extracting hour from the newly created time column
Order_Details['Hour'] = (Order_Details['Time']).dt.hour


# In[9]:


Order_Details


# In[16]:


## To get the most busy hour
time1 = Order_Details['Hour'].value_counts().index.tolist()[:24]


# In[21]:


## To get the frequency of purchase in busy hour
time2 = Order_Details['Hour'].value_counts().values.tolist()[:24]


# In[22]:


tmost = np.column_stack((time1,time2)) 

print(" Hour Of Day" + "\t" + "Cumulative Number of Purchases \n") 
print('\n'.join('\t\t'.join(map(str, row)) for row in tmost)) 


# In[23]:


timemost = Order_Details['Hour'].value_counts() 
print(timemost)
timemost1 = [] 

for i in range(0,23): 
    timemost1.append(i) 

timemost2 = timemost.sort_index() 
timemost2.tolist() 
timemost2 = pd.DataFrame(timemost2) 


# In[26]:


plt.figure(figsize=(20, 10)) 
  
plt.title('Sales Per Hour', 
          fontdict={'fontname': 'monospace', 'fontsize': 25},y= 1.05) 
  
plt.ylabel("Number Of Purchases Made", fontsize=18, labelpad=20) 
plt.xlabel("Hour", fontsize=18, labelpad=20) 
plt.plot(timemost1, timemost2, color='r') 
plt.grid() 
plt.show() 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




