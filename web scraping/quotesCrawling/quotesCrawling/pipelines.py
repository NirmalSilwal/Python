# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymongo


class QuotescrawlingPipeline:

    def __init__(self):
        # establishing connection with mongodb
        self.conn = pymongo.MongoClient('localhost', 27017)

        # creating database named 'myquotes'
        db = self.conn['myquotes']

        # creating collection
        self.collection = db['quotes_table']

    def process_item(self, item, spider):
        # print("Pipeline: " + item['title'][0])

        # storing item in database collection
        self.collection.insert(dict(item))
        return item
