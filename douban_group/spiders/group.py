# -*- coding: utf-8 -*-
import scrapy
# from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

from douban_group.items import DoubanGroupItem

class GroupSpider(scrapy.Spider):
    name = "group"
    allowed_domains = ["douban.com"]
    start_urls = (
        'http://www.douban.com/group/explore?tag=%E5%85%B4%E8%B6%A3',
        'http://www.douban.com/group/explore?tag=%E7%94%9F%E6%B4%BB',
        'http://www.douban.com/group/explore?tag=%E8%B4%AD%E7%89%A9',
        'http://www.douban.com/group/explore?tag=%E7%A4%BE%E4%BC%9A',
        'http://www.douban.com/group/explore?tag=%E8%89%BA%E6%9C%AF',
        'http://www.douban.com/group/explore?tag=%E5%AD%A6%E6%9C%AF',
        'http://www.douban.com/group/explore?tag=%E6%83%85%E6%84%9F',
        'http://www.douban.com/group/explore?tag=%E9%97%B2%E8%81%8A'
    )

    link_extractor = {
        # 'next_page': LinkExtractor(allow="/group/\w+/$"),
        # 'group_home_page': LinkExtractor(allow="/group/explore", restrict_xpaths="//span[@class='next']/a")
        'next_page': "//span[@class='next']/a/@href",
        'group_home_page': "//div[@class='result']/div[@class='content']/div[@class='title']/h3/a/@href"
    }

    _x_query = {
        'name': "//div[@id='group-info']/h1/text()",
        'members': "//div[@class='mod side-nav']/p/a/text()",
        'relative_groups': "//div[@class='bd']/div[@class='group-list']/div[@class='group-list-item']\
        /div[@class='title']/a/@href",
        'friend_groups': "//div[@class='obss']/div[@class='group-list']/div[@class='group-list-item']\
        /div[@class='title']/a/@href"
    }

    '''
    def parse(self, response):
        for link in self.link_extractor['next_page'].extract_links(response):
            print 'deal with next page %s', link.url
            yield scrapy.Request(url=link.url, callback=self.parse)

        for link in self.link_extractor['group_home_page'].extract_links(response):
            print 'deal with group home page %s', link.url
            yield scrapy.Request(url=link.url, callback=self.parse_group_home_page)
    '''

    def parse(self, response):
        for link in response.xpath(self.link_extractor['next_page']).extract():
            yield scrapy.Request(url=link, callback=self.parse)

        for link in response.xpath(self.link_extractor['group_home_page']).extract():
            yield scrapy.Request(url=link, callback=self.parse_group_home_page)

    def parse_group_home_page(self, response):
        i = ItemLoader(item=DoubanGroupItem(), response=response)
        i.add_xpath('group_name', self._x_query['name'])
        i.add_value('group_url', response.url)
        i.add_xpath('group_members', self._x_query['members'], re='\((\d+)\)')
        i.add_xpath('relative_groups', self._x_query['relative_groups'])
        i.add_xpath('friend_groups', self._x_query['friend_groups'])
        return i.load_item()
