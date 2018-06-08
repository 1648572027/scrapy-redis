# -*- coding: utf-8 -*-
import scrapy
import json

class FanyiSpider(scrapy.Spider):
    name = 'fanyi'
    allowed_domains = ['fanyi.baidu.com']
    start_urls = ['http://fanyi.baidu.com/sug/']

    def parse(self, response):

        text = response.text

        data = json.loads(text,encoding='utf-8')

        print('----------------------',data)
        yield data

        pass

    def start_requests(self):
        url = self.start_urls[0]

        world = input('请输入单词：')

        form = {'kw':world}

        request = scrapy.FormRequest(url=url,formdata=form,callback=self.parse)

        yield request

        # return super().start_requests()
