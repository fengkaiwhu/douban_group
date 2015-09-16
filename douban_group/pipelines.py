# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from douban_group import settings


class DoubanGroupPipeline(object):

    def __init__(self):
        self.server = settings.MONGO_SERVER
        self.db = settings.MONGO_DB
        self.coll = settings.MONGO_COLL
        self.group_info_coll = pymongo.MongoClient(self.server)[self.db][self.coll]

    def process_item(self, item, spider):
        self.group_info_coll.insert_one(dict(item))
        return item
