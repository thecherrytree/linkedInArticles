# Automated Extraction of LinkedIn Articles and their URLS
[Ben Teusch](https://www.linkedin.com/in/teuschb/), @Facebook People Analytics, [posted](https://www.linkedin.com/feed/update/urn:li:activity:6534214015349075968) on LinkedIn about wanting to perform a textual, thematic representation of article content from [David Green](https://www.linkedin.com/in/davidrgreen/), an author on LinkedIn. The goal was to extract content from the author, and also extract the articles this author linked to in their "top" and "best" article series. There are a few challenges in overcoming this automated extraction. In order to give maximum flexibility in extracting this content, I opted to use a selenium browser with beautiful soup to scrape articles. Though selenium is known for being a test automation software, it is perfect for when you are attempting to emulate a user in order to scrape content.

# Code
This was written in Python 3.7 using PyCharm. 

To run the code, you will need to import:
```
from supportingFunctions import *
```

The automation imports reside in the `supportingFunctions.py`.

Note: The secrets file referenced in `supportingFunctions.py` is used for automating authentication into linkedin using account credentials. If you submit a pull request on this code, please don't commit your account credentials. You can remove them from your files staged for commit by using: `git reset HEAD <secretsfile>`

# Get Involved:

If you would like to get involved, there are a few ways you can do so:
 - Fork the code and tinker around with the script on your own
 - Help build out a backlog of items that need to be worked on. You can visit the current backlog on the project board
    - This needs a front end, and also some scripting to clean up the article content and remove html within the article text
 - Ask to join the project if you want to contribute with pull requests
 - Submit issues if you discover bugs or think there are enhancements that would be beneficial to the project.
 - Submit ideas for future projects or datasets


# Links
I've set up a few resources to manage this project if you wish to contribute:
- [The post that started the project](https://www.linkedin.com/feed/update/urn:li:activity:6534214015349075968)
- [Project Board](https://github.com/thecherrytree/linkedInArticles/projects/1)
- [Excel File for David Green's Top/Best Articles](https://github.com/thecherrytree/linkedInArticles/blob/master/data/top_articles.csv)
- [CSV File for David Green's Article Text](https://github.com/thecherrytree/linkedInArticles/blob/master/data/davigrgreen_articles.csv)
- [My LinkedIn (if you want to connect/contribute)](https://www.linkedin.com/in/casoncherry/)


#Contributors
[Ben Teusch - Idea Originator](https://www.linkedin.com/in/teuschb/)
[@thecherrytree | Cason Cherry](https://www.linkedin.com/in/casoncherry/)