# Twitter_scraper
Scraper streamlit app to scrape tweets with no limits

i used snscrape https://github.com/JustAnotherArchivist/snscrape for this task

for the Scraping_data_program.py i used the dev version of snscrape by installing it using 
pip install git+https://github.com/JustAnotherArchivist/snscrape.git

With the development version, you can use the --jsonl argument, allowing you to access information directly from tweets instead of just tweet URLs, and to show the tweet content but this version can't be deployed with streamlit.

so for the Scraping_data_program2.py i used the last stable version, and it has been deployed with this link https://share.streamlit.io/attapalace/twitter_scraper/main/Scraping_data_program2.py


to run the app on your local machine you should write 'streamlit run Scraping_data_program.py' on your terminal, and be sure to have git installed in your machine
