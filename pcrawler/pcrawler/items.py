# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field

class PcrawlerItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = Field()
    street = Field()
    district = Field()
    city = Field()
    open_time = Field()
    close_time = Field()
    price = Field()
    point = Field()
    lat = Field()
    lon = Field()

