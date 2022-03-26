from csv import writer
from email import header
from bs4 import BeautifulSoup
import requests
url=("https://clutch.co/web-developers")
page=requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')
lists=soup.find_all('li', class_="provider")
with open('web_developer.csv','w',encoding='utf8',newline='') as f:
    thewriter = writer(f)
    header=['Comapny','Website','Location','Rating','Review Count','Hourly Rate','Min Project Size']
    thewriter.writerow(header)
    for list in lists:
        company_name=list.find('h3', class_="company_info").text.strip()
        company_website=list.find('a', class_="website-link__item")['href']
        company_location=list.find('span', class_="locality").text.strip()
        ratings=list.find('span', class_="sg-rating__number").text.strip()
        review_count=list.find('a', class_="sg-rating__reviews").text.strip()
        hourly_rate=list.find('div',class_="list-item custom_popover").span.text
        minimum_project_size=list.find('div', class_="list-item block_tag custom_popover").span.text
        avg_hourly_rate=list.find('div', class_="list-item custom_popover").span.text
        details=[company_name,company_website,company_location,ratings,review_count,hourly_rate,minimum_project_size]
        thewriter.writerow(details) 