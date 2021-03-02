## To setup your environment
`
pip install -r requirements.txt
`
## command to create the project

`
scrapy startproject quotesCrawling
`
## command to run the project

`
scrapy crawl quotes
`
> Note: make sure you install mongodb server. You can also install MongoDBCompass for your ease.

> And change the username and port number in MongoClient in **pipelines.py** file as per your Mongodb server. By default it will be **localhost** and **27017**
## command to share your installed python libraries

`
pip freeze > requirements.txt
`

