import scrapy
from tutorial.items import  TestItem
from scrapy.contrib.linkextractors import LinkExtractor

class LinkItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()


class LinksSpider(scrapy.Spider):
    name = "links"
    #allowed_domains = ["service.nsw.gov.au"]
    #start_urls = [
    #    "http://www.service.nsw.gov.au/transaction/renew-drivers-or-riders-licence",
    #]

    f = open("linklist.txt")
    start_urls = [url.strip() for url in f.readlines()]
    f.close()


    def parse(self, response):


        #items = []
        #
        url = response.url
        theTitle = response.selector.xpath('//title/text()').extract()

        item = LinkItem()
        item['url']=url
        item['title']=theTitle
        return item



