import scrapy
from tutorial.items import NswItem, TestItem
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from urlparse import urljoin


class NswSpider(CrawlSpider):
    name = "nsw"
    #allowed_domains = ["service.nsw.gov.au"]
    #start_urls = [
    #    "http://www.service.nsw.gov.au/transaction/renew-drivers-or-riders-licence"
    #]
    #rules = [
    #    Rule(LinkExtractor(),
    #     callback='parse_item', follow=True)
    #]

    def __init__(self, name=None, domain='', start=None, **kw):
        self.rules = [
            #Rule(LinkExtractor(allow=(domain)),callback='parse_item', follow=True)
            Rule(LinkExtractor(),callback='parse_item', follow=True)
            #Rule(LinkExtractor(),follow=True),
            #Rule(LinkExtractor(),callback='parse_item')
        ]
        self.start_urls = [start]
        self.allowed_domains = [domain]
        super(NswSpider, self).__init__(name, **kw)



    def parse_item(self, response):


        items = []

        url = response.url
        theTitle = response.selector.xpath('//title/text()').extract()


        for sel in response.xpath('//a'):

            item = NswItem()


            item['desc'] = sel.xpath('text()').extract()

            link = sel.xpath('@href').extract()[0]
            item['link'] = urljoin(response.url,link)

            item['pageTitle'] = theTitle
            item['pageUrl'] = url

            yield item

            #items.append(item)

        #return items

        '''

        url = response.url
        item = TestItem()
        item['url'] = url
        return item
    '''






