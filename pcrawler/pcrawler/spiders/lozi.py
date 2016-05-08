# -*- coding: utf-8 -*-
import json
import scrapy
from scrapy.http import Request
from pcrawler.items import PcrawlerItem


class LoziSpider(scrapy.Spider):
    name = "lozi"
    allowed_domains = ["lozi.vn"]
    start_urls = (
        'http://latte.lozi.vn/v1/search/eateries?q=ph%E1%BB%9F'
        '&cityId=1&t=popular&skip=20&limit=20',
    )

    def parse(self, response):
        for url in ['http://latte.lozi.vn/v1/search/eateries?q=ph%E1%BB%9F'
                    '&cityId=1&t=popular&skip={0}&limit=20'.format(count)
                    for count in range(20, 1701, 20)]:
            yield Request(url, callback=self.parse_item)

    def parse_item(self, response):
        response_info = json.loads(response.body)['data']
        item = PcrawlerItem()

        for info in response_info:
            item['name'] = info['name']
            item['street'] = info['address']['street']
            item['district'] = info['address']['district']
            item['city'] = info['address']['city']
            item['address'] = info['address']['full']
            item['lat'] = info['latitude']
            item['lon'] = info['longitude']
            try:
                item['open_time'] = info['operatingTime'][0]['start']
                item['close_time'] = info['operatingTime'][0]['finish']
            except:
                item['open_time'] = ''
                item['close_time'] = ''
            item['open_close'] = item['open_time'] + "-" + item['close_time']
            item['price'] = info['priceCouple']/2
            item['ratings'] = info['rating']

            return item
