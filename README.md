# Automated Extraction of LinkedIn Articles and their URLS
[Ben Teusch](https://www.linkedin.com/in/teuschb/), @Facebook People Analytics, [posted](https://www.linkedin.com/feed/update/urn:li:activity:6534214015349075968) on LinkedIn about wanting to perform a textual, thematic representation of article content from [David Green](https://www.linkedin.com/in/davidrgreen/), an author on LinkedIn. The goal was to extract content from the author, and also extract the articles this author linked to in their "top" and "best" article series. There are a few challenges in overcoming this automated extraction. In order to give maximum flexibility in extracting this content, I opted to use a selenium browser with beautiful soup to scrape articles. Though selenium is known for being a test automation software, it is perfect for when you are attempting to emulate a user in order to scrape content.

# Code
This was written in Python 3.7 using PyCharm. 

To run the code, you will need to import:
```
from supportingFunctions import *
```

The automation imports reside in the `supportingFunctions.py`.

###Get Started
1. You can simply view the data in the [data folder](https://github.com/thecherrytree/linkedInArticles/blob/master/data/)
2. Clone the repository
3. Ensure you have a python environment setup (PyCharm community is fine, you can also use VSCode or others...)
4. Set up your own secrets file and import your secrets as variables
5. Run the script to watch the selenium browser scrape data
6. You can comment out `#build out the file of david greens articles (davidrgreen_articles.csv) in the data folder.
supportingFunctions.build_article_file_of_david_green_articles(articles, browser)` in the `__init__.py` to skip the creation of the file


Note: The secrets file referenced in `supportingFunctions.py` is used for automating authentication into linkedin using account credentials. If you submit a pull request on this code, please don't commit your account credentials. You can remove them from your files staged for commit by using: `git reset HEAD <secretsfile>`

# Get Involved

If you would like to get involved, there are a few ways you can do so:
 - Fork the code and tinker around with the script on your own
 - Help build out a backlog of items that need to be worked on. You can visit the current backlog on the project board
    - This needs a front end, and also some scripting to clean up the article content and remove html within the article text
 - Ask to join the project if you want to contribute with pull requests
 - Submit issues if you discover bugs or think there are enhancements that would be beneficial to the project.
 - Submit ideas for future projects or datasets
 - If you prefer to work on a parallel project done in R, visit project by Keith McNulty in the links below


# Links
Below are a few resources to manage this project if you wish to get involved:
- [Review the post that started the project](https://www.linkedin.com/feed/update/urn:li:activity:6534214015349075968)
- [Project Board to submit issues & requests](https://github.com/thecherrytree/linkedInArticles/projects/1)
- [CSV File for David Green's Top/Best Articles](https://github.com/thecherrytree/linkedInArticles/blob/master/data/top_articles.csv)
- [CSV File for David Green's 108 Articles and their text](https://github.com/thecherrytree/linkedInArticles/blob/master/data/davigrgreen_articles.csv)
- [My LinkedIn (if you want to connect/contribute)](https://www.linkedin.com/in/casoncherry/)
- [View the RShiny App in progress by Keith McNulty](https://github.com/keithmcnulty/david_green_webscraping)


# Contributors
[Ben Teusch - Idea Originator](https://www.linkedin.com/in/teuschb/)

[@keithmcnulty](https://github.com/keithmcnulty) | [Keith McNulty](https://www.linkedin.com/in/keith-mcnulty/) for his RShiney webscraper

[@thecherrytree](https://github.com/thecherrytree) |[Cason Cherry](https://www.linkedin.com/in/casoncherry/)
