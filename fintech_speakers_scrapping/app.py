from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# import time
# import requests
import csv

driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))
driver.get('file:///E:/Infoware/fintech_speakers_scrapping/Top%20Fintech%20Speakers%20in%20India%20_%20Global%20Fintech%20Fest.-htmlhtml.html')

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')
dialog_div = soup.find('div', class_='dialog-off-canvas-main-canvas')
container_div = dialog_div.select_one('.content .graybg .w-100 .layout .col-lg-12 .views-element-container .content .js-view-dom-id-152c41b0c097451823567e70a8a7b211c5ee7e5ea45289424686ed45dc29c973 .row')

speakers = container_div.select('div.col-6.col-lg-3')

for speaker in speakers:
    speaker_name = speaker.find('h4').text.strip()
    company_name = speaker.find_all('p')[1].text.strip()  # Assuming the company name is the second <p> element
    linkedin_element = speaker.find('a', class_='card--linkedinimg')
    if linkedin_element:
        linkedin_url=linkedin_element['href']
    else:
        linkedin_url='na'
    log_data=[speaker_name,company_name,linkedin_url]
    with open('speakers_log.csv','a',newline='') as file:
        writer=csv.writer(file)
        writer.writerow(log_data)