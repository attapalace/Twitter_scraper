#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os
import pandas as pd
import streamlit as st
from datetime import date


# In[9]:


#pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_rows', None)


# In[6]:


today = date.today()
st.markdown('if you want to search for either of multiple terms write as (cats OR dogs)')
search_term = st.text_input('Enter your search term')
from_date = st.text_input('Enter starting date as 2020-06-01 foramt', '2020-06-01')
until_date = st.text_input('Enter end date as 2021-06-01 foramt',today)

if st.button('show number of tweets'):  
    if search_term:
        os.system(f"snscrape --since {from_date} twitter-search '{search_term} until:{until_date}' > result-tweets.txt")
        tweets_df2 = pd.read_csv('result-tweets.txt')
        st.markdown('Number Of Tweets :'+ str(tweets_df2.size))

