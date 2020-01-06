# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


from indeed_scraper.settings import MONGODB_SERVER,MONGODB_DB,MONGODB_COLLECTION
import pymongo
from scrapy.exceptions import DropItem
import logging

class JobsScrapyPipeline(object):
    
    def __init__(self):
        connection = pymongo.MongoClient(
            MONGODB_SERVER
        )
        db = connection[MONGODB_DB]
        self.collection = db[MONGODB_COLLECTION]


    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            job_titl = item['title']
            company_nam = item['staticCompanyName']
            
            checking = self.collection.find_one({"title":job_titl,"staticCompanyName":company_nam})
            if checking is None:
                self.collection.insert(dict(item))
            else:
                print("============================================================already exists=============================================")
        return item
