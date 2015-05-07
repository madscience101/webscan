import scrapy
from tutorial.items import DmozItem
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from urlparse import urljoin
import os


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["service.nsw.gov.au"]
    start_urls = [
        "http://www.service.nsw.gov.au/transaction/renew-drivers-or-riders-licence",
    ]


    def parse(self, response):

        theTitle = response.selector.xpath('//title/text()').extract()

        for sel in response.xpath('//a'):

            item = DmozItem()

            item['title'] = sel.xpath('text()').extract()
            item['link'] = sel.xpath('@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item
            print item
