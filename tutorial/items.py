# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()


class TestItem(scrapy.Item):
    url = scrapy.Field()


class NswItem(scrapy.Item):
    pageUrl = scrapy.Field()
    pageTitle = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()