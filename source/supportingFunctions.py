import csv
import time
import secrets
from bs4 import BeautifulSoup
from selenium import webdriver


def start_browser_and_login(loginUrl):
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
    return browser

def browser_scroll(browser):
    while True:
        # Get scroll height.
        last_height = browser.execute_script("return document.body.scrollHeight")
        # Scroll down to the bottom.
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load the page.
        time.sleep(2)
        # Calculate new scroll height and compare with last scroll height.
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def parse_html(browser):
    html = browser.execute_script("return document.body.innerHTML;")
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def build_article_file_of_david_green_articles(articles, browser):
    with open('../data/davigrgreen_articles.csv', mode='w') as csv_file:
        fieldnames = ['author', 'date', 'title', 'url', 'content']
        writer = csv.DictWriter(csv_file, delimiter=',', fieldnames=fieldnames)
        for article in articles:
            author = 'David R. Green'
            url = 'https://www.linkedin.com'
            atags = article.findAll('a')
            for a in atags:
                url += a['href']
            date = article.select('time')[1].text.strip()
            title = article.select('h1')[0].text.strip()
            browser.get(url)
            soup = supportingFunctions.parse_html(browser)
            articles = soup.find("div", {"class": "reader-article-content"})
            # Grabbing the article content from David Green's parent articles (these are likely summaries of his articles) for his "top" and "best" series
            content = articles.find_all("p")
            # otherArticlesP = content
            # otherArticlesh3 = articles.find_all("h3")
            # for a in otherArticlesP:
            #     print(a)
            # print({'author': author, 'date': date, 'title': title, 'url': url, 'content': content})
            writer.writerow({'author': author, 'date': date, 'title': title, 'url': url, 'content': content})
            # no, I'm not a script because I wait for a little while
            time.sleep(2)