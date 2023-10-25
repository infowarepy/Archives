from googlesearch import search
from bs4 import BeautifulSoup
import requests

query='cybersecurity policy/strategy news in singapore'

news_links=[]
c=0
for link in search(query, tld="co.in", num=1, stop=40, pause=1):
    news_links.append(link)
    c=c+1
    print(c,end='\r')

for news_link in news_links:
    print(news_link)

# url = "https://www.channelnewsasia.com/singapore/singapore-proactive-stance-cyber-threats-updated-national-strategy-2223536"
url='https://www.kcl.ac.uk/study/postgraduate-taught/courses/cyber-policy-strategy-ma'
n=0
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    page_content = soup.prettify()
    n=n+1
    # print(page_content)
else:
    print("Failed to retrieve the webpage.")

print('No of links = ',n)
print('No of tracable links=',c)
