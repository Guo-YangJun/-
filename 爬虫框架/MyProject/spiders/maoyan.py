# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from MyProject.items import MyprojectItem

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = []
    base_url = 'https://maoyan.com/cinemas?offset=%d'
    for i in range(0,240,12):
        url = base_url%i
        start_urls.append(url)

    def parse(self, response):
        obj = response.body.decode('utf-8')
        data = etree.HTML(obj)
        all = data.xpath('//div[@class="cinema-info"]')
        for i in all:
            item = MyprojectItem()
            name = i.xpath('.//a/text()')[0]
            print(name)
            item['name'] = name
            address = i.xpath('.//p/text()')[0]
            item['address'] = address
            print(address)
            yield item