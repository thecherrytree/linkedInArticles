import csv
from supportingFunctions import *

loginUrl = 'https://www.linkedin.com/login'
resultsUrl = 'https://www.linkedin.com/in/davidrgreen/detail/recent-activity/posts/'

browser = supportingFunctions.start_browser_and_login(loginUrl)
browser.get(resultsUrl)

#scroll the browser (we need this to get dynamicall loaded content) to the bottom to get all available articles...this could take a few minutes.
supportingFunctions.browser_scroll(browser)

#get the html content from the fully scrolled browser
soup = supportingFunctions.parse_html(browser)
#extract <article> tags from html content
articles = soup.find_all("article")

#build out the file of david greens articles (davidrgreen_articles.csv) in the data folder.
supportingFunctions.build_article_file_of_david_green_articles(articles, browser)


