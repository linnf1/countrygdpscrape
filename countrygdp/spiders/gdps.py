# -*- coding: utf-8 -*-
import scrapy
# initialize w/  scrapy crawl gdps

class GdpsSpider(scrapy.Spider):
    name = 'gdps'
    allowed_domains = ['worldpopulationreview.com']
    start_urls = ['http://worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        rows = response.xpath("//table/tbody/tr")
        for row in rows:
            yield {
                'cname': row.xpath(".//td[1]/a/text()").get(),
                'gdpdebt': row.xpath(".//td[2]/text()").get()
            }