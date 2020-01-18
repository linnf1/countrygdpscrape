# -*- coding: utf-8 -*-
import scrapy


class GdpsSpider(scrapy.Spider):
    name = 'gdps'
    allowed_domains = ['worldpopulationreview.com']
    start_urls = ['http://worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        gdps = response.xpath("")
        
        pass
