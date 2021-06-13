

import os
import pandas as pd
import streamlit as st
from datetime import date


#pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_rows', None)



today = date.today()
st.markdown('if you want to search for either of multiple terms write between brackets as (cats OR dogs)')
search_term = st.text_input('Enter your search term')
from_date = st.text_input('Enter starting date as 2020-06-01 foramt', '2020-06-01')
until_date = st.text_input('Enter end date as 2021-06-01 foramt',today)

max_results= st.text_input('if you want to show the tweets write the max tweets to display', 100)

if st.button('show number of tweets'):  
    if search_term:
        os.system(f"snscrape --jsonl --since {from_date} twitter-search '{search_term} until:{until_date}' > result-tweets.json")
        tweets_df2 = pd.read_json('result-tweets.json', lines=True)
        st.markdown('Number Of Tweets :'+ str(tweets_df2.shape[0]))

if st.button('show tweets'):  
    if search_term:
        os.system(f"snscrape --jsonl --max-results {max_results} --since {from_date} twitter-search '{search_term} until:{until_date}' > result-tweets.json")
        tweets_df2 = pd.read_json('result-tweets.json', lines=True)
        for row in tweets_df2['content'].iteritems():
            st.text(row)

