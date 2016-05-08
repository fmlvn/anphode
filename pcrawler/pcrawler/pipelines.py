# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import requests


RESTAURANT_ENDPOINT = 'http://127.0.0.1:5000/restaurant'


class PcrawlerPipeline(object):
    def process_item(self, item, spider):
        requests.post(RESTAURANT_ENDPOINT, json=item._values)
