import scrapy
from tutorial.items import DmozItem
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from urlparse import urljoin


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["service.nsw.gov.au"]
    start_urls = [
        "http://www.service.nsw.gov.au/",
    ]

    def parse(self, response):
        for sel in response.xpath('//a'):

            item = DmozItem()

            #title = sel.xpath('a/text()').extract()
            #link = sel.xpath('a/@href').extract()
            #desc = sel.xpath('text()').extract()
            ##yield item
            #print title, link, desc


            item['title'] = sel.xpath('text()').extract()
            #item['link'] = sel.xpath('@href').extract()
            link = sel.xpath('@href').extract()
            item['link'] = urljoin(response.url,link[0])
            item['desc'] = sel.xpath('text()').extract()

            yield item