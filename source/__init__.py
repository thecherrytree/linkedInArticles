import csv
import time
import secrets
from bs4 import BeautifulSoup
import selenium.common.exceptions
from selenium import webdriver

loginUrl = 'https://www.linkedin.com/login'
resultsUrl = 'https://www.linkedin.com/in/davidrgreen/detail/recent-activity/posts/'

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option('useAutomationExtension', False)
browser = webdriver.Chrome(options=chromeOptions,
                           desired_capabilities=chromeOptions.to_capabilities())
browser.get(loginUrl)
browser.execute_script(
    "document.getElementById('username').setAttribute('value', '" + secrets.username + "')")
browser.execute_script(
    "document.getElementById('password').setAttribute('value', '" + secrets.password + "')")
browser.find_element_by_xpath('//*[@id="app__container"]/main/div/form/div[3]/button').click()
browser.get(resultsUrl)
# Get scroll height.
last_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to the bottom.
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load the page.
    time.sleep(2)
    # Calculate new scroll height and compare with last scroll height.
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
html = browser.execute_script("return document.body.innerHTML;")
soup = BeautifulSoup(html, 'html.parser')
articles = soup.find_all("article")

with open('davigrgreen_articles.csv', mode='w') as csv_file:
    fieldnames = ['author', 'date', 'title', 'url']
    writer = csv.DictWriter(csv_file, delimiter=',', fieldnames=fieldnames)
    for article in articles:
        author = 'David R. Green'
        url = 'https://www.linkedin.com/'
        atags = article.findAll('a')
        for a in atags:
            url += a['href']
        date = article.select('time')[1].text.strip()
        title = article.select('h1')[0].text.strip()
        writer.writerow({'author': author, 'date': date, 'title': title, 'url':url})

