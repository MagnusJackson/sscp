#!/usr/bin/env python
# coding: utf-8
# Author: Dhruv Pathak

# # To Create an application to parse the JSON from the given API
# ### API: https://s3.amazonaws.com/open-to-cors/assignment.json

# In[1]:


#Importing necessary libraries
import json #for accessing the json file
import pandas as pd #for storing the json file data to a dataframe
import requests #used to send HTTP request to the API
from tabulate import tabulate #for presentation of the dataframe

API_KEY = "my-api-key" #used to track the usage of the API (optional, but recommended)

base_url = "https://s3.amazonaws.com/open-to-cors/assignment.json?api-key="+API_KEY
list_req = requests.get(base_url).json()

df = pd.DataFrame(i for i in list_req['products'].values()) #converting the data to a pandas dataframe

print(tabulate(df[['title','price']], headers = 'keys', tablefmt = 'fancy_grid')) #displaying the dataframe using 'tabulate'


# Here below, I have used another method of presentation of data by using the style function of pandas.

# In[2]:


def color_subcategory(val):
    if val == 'tablet':
        color = 'blue' 
    elif val == 'smart-watches':
        color = 'red'
    elif val == 'fitness-tracker':
        color = 'green'
    else:
        color = 'black'
    return 'color: % s' % color

df.style.applymap(color_subcategory) 


# Please note that the different subcategories have been marked with different colors

# In[ ]:




