# Automated Extraction of LinkedIn Articles and their URLS
A LinkedIn user recently wanted to perform a textual, thematic representation of article content from a specific author on LinkedIn. The goal was to extract content from the author, and also extract the articles this author linked to in their "top" and "best" article series. There are a few challenges in overcoming this automated extraction. In order to give maximum flexibility in extracting this content, I opted to use a selenium browser with beautiful soup to scrape articles. Though selenium is known for being a test automation software, it is perfect for when you are attempting to emulate a user in order to scrape content.

# Code
This was written in Python 3.7 using PyCharm. 

To run the code, you will need to import:
```
from supportingFunctions import *
```

The automation imports reside in the `supportingFunctions.py`.

Note: The secrets file referenced in `supportingFunctions.py` is used for automating authentication into linkedin using account credentials. If you submit a pull request on this code, please don't commit your account credentials. You can remove them from your files staged for commit by using: `git reset HEAD <secretsfile>`

# Links
I've set up a few resources to manage this project if you wish to contribute:
- [Project Board](https://github.com/thecherrytree/linkedInArticles/projects/1)
- [Excel File for David Green's Top/Best Articles](https://github.com/thecherrytree/linkedInArticles/blob/master/data/top_articles.xlsx)
- [CSV File for David Green's Article Text](https://github.com/thecherrytree/linkedInArticles/blob/master/data/davigrgreen_articles.csv)
- [My LinkedIn (if you want to connect/contribute)](https://www.linkedin.com/in/casoncherry/)
