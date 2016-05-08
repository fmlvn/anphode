# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class PcrawlerItem(Item):
    name = Field()
    street = Field()
    district = Field()
    city = Field()
    open_time = Field()
    address = Field()
    close_time = Field()
    open_close = Field()
    price = Field()
    ratings = Field()
    lat = Field()
    lon = Field()
