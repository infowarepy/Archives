from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import requests
import csv

def find_sectors(exhibitor_item):
    sector_ul = exhibitor_item.find('ul', class_='sector_block')
    if sector_ul:
        sector_items = sector_ul.find_all('li')
        sectors = [item.get_text(strip=True) for item in sector_items]
    else:
        sectors = 'N/A'
    return sectors

def find_website(exhibitor_item):
    button = exhibitor_item.select_one('.caption .button_block.text-right .btn')
    if button and 'href' in button.attrs:
        profile_link = button['href']
    else:
        profile_link = None
    response = requests.get(profile_link)
    soup = BeautifulSoup(response.text, 'html.parser')
    website_link_element = soup.find('li', class_='social_website')
    if website_link_element:
        website_link = website_link_element.a['href']
    else:
        website_link = "N/A"
    return website_link

#The driver opens the target link and scrolls down until full list is loaded.
driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))
driver.get('https://exhibitors.expandnorthstar.com/north-star-2023/Exhibitor')# Scroll down to load more content
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    print('hello')
    time.sleep(2)
    
    load_data_message = driver.find_element("id","load_data_message")
    if load_data_message and "no more content available" in load_data_message.text.lower():
        break

print('loading successful')

#Extracting page source for scrapping
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')
container = soup.find('div', class_='container-fluid mian')

#Doing scrapping of particular 'container'
if container:
    category_listing = container.find('div', id='category_listing')

    if category_listing:
        load_data = category_listing.find('div', id='load_data')
        exhibitor_items = load_data.select('div.item.col-12.list-group-item')

        #iterating throgh each exhibitor
        for exhibitor_item in exhibitor_items:
            name = exhibitor_item.select_one('.item_heading h4').text.strip()
            country=exhibitor_item.select_one('.item_heading span').text.strip()
            sectors=find_sectors(exhibitor_item)
            website_link = find_website(exhibitor_item)
            
            log_data=[name,country,sectors,website_link]

            #storing log data into a csv file
            print(log_data)
            with open("new_log.csv", "a",newline='') as f:
                writer = csv.writer(f)
                writer.writerow(log_data)

driver.quit()