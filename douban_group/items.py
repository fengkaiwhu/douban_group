# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanGroupItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 小组名称
    group_name = scrapy.Field()
    # 小组对应的url
    group_url = scrapy.Field()
    # 小组的人数
    group_members = scrapy.Field()
    # 友情小组
    friend_groups = scrapy.Field()
    # 相关小组
    relative_groups = scrapy.Field()
