import scrapy
from tutorial.items import TestItem
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

class TestSpider(CrawlSpider):
    name = "testme"
    allowed_domains = ["www.service.nsw.gov.au"]
    start_urls = [
        "http://www.service.nsw.gov.au/"
    ]
    rules = [
        #Rule(LinkExtractor(deny=("facilities.arts.nsw.gov.au")),
        # callback='parse_item', follow=True)

        Rule(LinkExtractor(),
         callback='parse_item', follow=True)

    ]


    def parse_item(self, response):

        url = response.url
        item = TestItem()
        item['url'] = url

        #print url

        return item