import supportingFunctions
import csv
from supportingFunctions import *

loginUrl = 'https://www.linkedin.com/login'
resultsUrl = 'https://www.linkedin.com/in/davidrgreen/detail/recent-activity/posts/'

browser = supportingFunctions.start_browser_and_login(loginUrl)


# browser.get(resultsUrl)
# #scroll the browser (we need this to get dynamically loaded content) to the bottom to get all available articles...this could take a few minutes.
# supportingFunctions.browser_scroll(browser)
# #get the html content from the fully scrolled browser
# soup = supportingFunctions.parse_html(browser)
# #extract <article> elements from html content
# articles = soup.find_all("article")
# #build out the file of david greens articles (davidrgreen_articles.csv) in the data folder.
# supportingFunctions.build_article_file_of_david_green_articles(articles, browser)

#read in the top_articles for david green
top_articles = supportingFunctions.read_in_top_articles()

#grab URLS from data in file and direct the browser to get anchors from David Green article
i=0
with open('../data/david_green_top_best_articles', mode='w') as csv_file:
    fieldnames = ['reference_article', 'title', 'author', 'url', 'content']
    writer = csv.DictWriter(csv_file, delimiter=',', fieldnames=fieldnames)
    writer.writeheader()
    for url in top_articles['URL']:
        reference_article = top_articles['Title'][i]
        browser.get(url)
        soup = supportingFunctions.parse_html(browser)
        article_content = soup.find_all('div',  {"class": "reader-article-content"})
        supportingFunctions.determine_article_structure_and_parse(article_content, reference_article, writer)
        csv_file.flush()
        i += 1