# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymongo


class FlipcartcrawlingPipeline:

    def __init__(self):
        # establishing connection with mongodb
        #using local host
        self.conn = pymongo.MongoClient('localhost', 27017)

        # using mongo atlas, in cloud
        # self.conn = pymongo.MongoClient('your database connection URL here')

        # creating database
        db = self.conn['remoteDbNirmal']

        # creating collection
        self.collection = db['flipcart']

    def process_item(self, item, spider):

        # storing item in database collection
        self.collection.insert(dict(item))

        return item
