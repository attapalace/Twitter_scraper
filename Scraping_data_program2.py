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
st.markdown('if you want to search for either of multiple terms write as (cats OR dogs), if you want to search for exact phrase write "cats and dogs"')
search_term = st.text_input('Enter your search term')
from_date = st.text_input('Enter starting date as 2020-06-01 foramt', '2020-06-01')
until_date = st.text_input('Enter end date as 2021-06-01 foramt',today)
max_results= st.text_input('if you want to show the tweets write the max tweets to display', 100)


if st.button('show number of tweets'):  
    if search_term:
        os.system(f"snscrape --since {from_date} twitter-search '{search_term} until:{until_date}' > result-tweets.txt") 
        s = 0
        if os.stat("result-tweets.txt").st_size == 0:
            s = 0
        else:
            tweets_df2 = pd.read_csv('result-tweets.txt',names = ['link'])
            s = tweets_df2.size
            
        st.markdown('Number Of Tweets :'+ str(s))

if st.button('show tweets'):
    if search_term:
        all_s = "snscrape --format '{content!r}'"+ f" --max-results {max_results} --since {from_date} twitter-search '{search_term} until:{until_date}' > result-tweets.txt"
        os.system(all_s)
        if os.stat("result-tweets.txt").st_size == 0:
            st.text('No tweets found')
        else:
            tweets_df2 = pd.read_csv('result-tweets.txt', names=['content'])
            for row in tweets_df2['content'].iteritems():
                st.text(row)
            st.markdown('Number Of Tweets :'+ str(tweets_df2.size))
