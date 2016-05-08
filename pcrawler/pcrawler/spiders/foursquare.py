# -*- coding: utf-8 -*-
import scrapy


class FoursquareSpider(scrapy.Spider):
    name = "foursquare"
    allowed_domains = ["foursquare.com"]
    start_urls = (
        'http://www.foursquare.com/',
    )

    def parse(self, response):
        pass
