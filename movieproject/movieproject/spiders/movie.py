# -*- coding: utf-8 -*-
import scrapy
from ..items import    MovieprojectItem

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['www.dy2018.com']
    start_urls = ['https://www.dy2018.com/0/']

    def parse(self, response):

        tables = response.xpath('//table[@class="tbspan"]')

        for t in tables:

            item = MovieprojectItem()

            title = t.xpath('.//tr[2]//a[2]/text()').extract()[0]

            info = ''.join(t.xpath('.//tr[4]//p/text()').extract())

            info = info.replace('\u3000','')

            item['title'] = title

            item['info'] = info

            yield item


