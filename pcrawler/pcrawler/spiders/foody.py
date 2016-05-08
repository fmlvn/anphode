# -*- coding: utf-8 -*-
import scrapy

from scrapy.http import Request
from pcrawler.items import PcrawlerItem


class FoodySpider(scrapy.Spider):
    name = "foody"
    allowed_domains = ["foody.vn"]
    start_urls = (
        'https://foody.vn',
    )

    def parse(self, response):
        # Get the next page and yield Requests
        for url in ['https://www.foody.vn/ha-noi/dia-diem?ds=Restaurant&vt=row\
                    &st=1&q=ph%E1%BB%9F&dt=undefined&page={0}&provinceId=218\
                    &categoryId=null&append=true'.format(count)
                    for count in range(1, 444)]:
            yield Request(url)

        # Get urls in page and yield Requests
        url_selector = response.xpath('*//div[@class="result-name"]/'
                                      'h2/a/@href').extract()
        for url in url_selector:
            yield Request("https://www.foody.vn" + url,
                          callback=self.parse_item)

    def parse_item(self, response):
        # Get data from detail page and yield to items
        item = PcrawlerItem()

        item['name'] = response.xpath('*//div[@class="main-info-title"]/'
                                      'h1/text()').extract()[0]
        item['street'] = response.xpath('//div[@class="res-common-add"]/'
                                        'span[2]/a/text()').extract()[0]
        item['district'] = response.xpath('//div[@class="res-common-add"]/'
                                          'span[3]/a/text()').extract()[0]
        item['city'] = response.xpath('//div[@class="res-common-add"]/'
                                      'span[4]/text()').extract()[0]
        try:
            item['close_time'] = response.xpath('*//span[@style="margin-left: '
                                                '5px;"]/span/span[2]/text()'
                                                ).extract()[0]
            item['open_time'] = response.xpath('*//span[@style="margin-left: '
                                               '5px;"]/span/span[1]/text()'
                                               ).extract()[0]
            item['price'] = response.xpath('*//div[@class='
                                           '"res-common-minmaxprice"]/'
                                           'span/span/text()'
                                           ).extract()[0].split()[0]
            item['price'] += "-"
            item['price'] += response.xpath('*//div[@class='
                                            '"res-common-minmaxprice"]/'
                                            'span/span/span/text()'
                                            ).extract()[0]
        except:
            item['close_time'] = ''
            item['open_time'] = ''
            item['price'] = ''
        item['point'] = response.xpath('*//div[@class="ratings-boxes-points"]'
                                       '/div/span/b/text()').extract()[0]
        item['lat'] = response.xpath('//meta[@property='
                                     '"place:location:latitude"]/@content'
                                     ).extract()[0]
        item['lon'] = response.xpath('//meta[@property='
                                     '"place:location:longitude"]/@content'
                                     ).extract()[0]

        return item
