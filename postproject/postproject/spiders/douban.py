# -*- coding: utf-8 -*-
import scrapy
import urllib
import urllib.request
from PIL import Image

from scrapy_redis.spiders import Spider,CrawlSpider

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['www.douban.com']
    start_urls = ['https://www.douban.com/accounts/login']

    def parse(self, response):

        captcha_url = response.xpath('//img[@id="captcha_image"]/@src').extract_first()

        if not captcha_url:
            username = '18513106743'
            pwd = '31415926abc'
            form = {'email': username,
                    'password': pwd
                    }
            pass
        else:
            urllib.request.urlretrieve(captcha_url,'./captcha.png')
            Image.open('./captcha.png').show()

            code = input('请输入验证码：')
            username = '18513106743'
            pwd = '31415926abc'

            form = {'email':username,
                    'password':pwd,
                    'captcha':code}

        post_url = 'https://www.douban.com/login'
        yield scrapy.FormRequest(url=post_url,formdata=form,callback=self.parse_post)
        pass

    def parse_post(self,response):
        text = response.text

        person_url = 'https://www.douban.com/people/164698173'

        yield scrapy.Request(url=person_url,callback=self.parse_person)

    def parse_person(self,response):
        pass


