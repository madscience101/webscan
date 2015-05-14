import scrapy
from tutorial.items import NswItem, TestItem
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from urlparse import urljoin


class AllNswSpider(CrawlSpider):
    name = "allnsw"

    #allowed = ".gov.au"


    def __init__(self, name=None,  domain='',start = '', filename='', **kw):
        self.rules = [
            #Rule(LinkExtractor(allow=(domain)),callback='parse_item', follow=True)
            Rule(LinkExtractor(),callback='parse_item', follow=True)
            #Rule(LinkExtractor(),follow=True),
            #Rule(LinkExtractor(),callback='parse_item')
        ]

        self.start_urls = [start]
        self.allowed_domains = [domain]

        super(AllNswSpider, self).__init__(name, **kw)



    def parse_item(self, response):

        try:
            for sel in response.xpath('//a'):

                item = TestItem()

                href = sel.xpath('@href').extract()
                if (len(href) > 0):
                    link = sel.xpath('@href').extract()[0]
                    item['url'] = link
                    yield item
        except:
            pass

            #items.append(item)

        #return items
