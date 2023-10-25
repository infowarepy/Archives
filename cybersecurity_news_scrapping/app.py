from google import search
from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv


def extract_news(country):
    query=f"cybersecurity policy/strategy news in \"{country}\""
    print('>>>',query)
    news_links=[]
    c=0
    for link in search(query, tld="co.in", num=1, stop=10, pause=2,tbs='qdr:w'):
        news_links.append(link)
        c=c+1
        print('Links fetched:',c,end='\r')

    return news_links

def log_data(cnt):
    for country in cnt["Country_Name"]:
        news_links=extract_news(country)
        log_data=[country,news_links]
        with open("news_links.csv", "a",newline='') as f:
                writer = csv.writer(f)
                writer.writerow(log_data)

cnt = pd.read_csv('country.csv')
log_data(cnt)