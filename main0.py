import pandas as pd
from newsapi import NewsApiClient
import random
# Paediatric
# aa9b869592d846948528369252d4cd54

newsapi = NewsApiClient(api_key="aa9b869592d846948528369252d4cd54")


dataframe = pd.read_csv('data.csv')
# ['HOSP_NAME','HOSP_TYPE','DISTRICT_NAME','SPECIALTY_NAME','HOSP_CONTACT_NO','HOSP_EMAIL_ID','HOSP_ADDRESS']

def filter(col,text):
    return dataframe[col].astype(str).str.lower().astype(str).str.contains(text.lower())
def Search(dataframe,text):
    return dataframe[filter('HOSP_NAME',text) | filter('HOSP_TYPE',text) | filter('DISTRICT_NAME',text) | filter('SPECIALTY_NAME',text) | filter('HOSP_CONTACT_NO',text) | filter('HOSP_EMAIL_ID',text) | filter('HOSP_ADDRESS',text)]

# print(Search(dataframe, 'General surgery'))
# print(dataframe)

def Feed(no):
    news = newsapi.get_everything(q="World Health Organisation", page=no, page_size=20)
    return  sorted(news['articles'], key=lambda x: random.random())

print()