# -*- coding: utf-8 -*-
import scrapy

from MyProject.items import MeiJu
class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['meijutt.com']
    start_urls = ['https://www.meijutt.com/new100.html']

    def parse(self, response):
        with open('美剧.html','a',encoding = 'utf-8')as f:
            f.write(response.body.decode('gb2312'))
        all = response.xpath('//ul[@class="top-list  fn-clear"]/li')
        for i in all:
            meiju = MeiJu()
            mc = i.xpath('.//h5//text()').extract()[0]
            zm = i.xpath('.//span[1]//text()').extract()
            lx = i.xpath('.//span[2]//text()').extract()[0]
            dst = i.xpath('.//span[3]//text()').extract()[0]
            sj = i.xpath('.//div[@class="lasted-time new100time fn-right"]//text()').extract()[0]
            tz = i.xpath('.//h5/a/@href').extract()[0]
            base_url = 'https://www.meijutt.com/'
            url =base_url+tz
            meiju['mc'] = mc
            meiju['zm'] = zm
            meiju['lx'] = lx
            meiju['dst'] = dst
            meiju['sj'] = sj
            meiju['url'] = url
            yield scrapy.Request(url = url,callback = self.meiju,meta = {"meiju":meiju})
    def meiju(self, response):
        meiju = response.meta['meiju']
        bm = response.xpath('//div[@class="o_r_contact_all"]/div[2]/ul/li[2]//text()').extract()
        sysj = response.xpath('//div[@class="o_r_contact_all"]/div[2]/ul/li[6]//text()').extract()
        meiju['bm'] = bm
        meiju['sysj'] = sysj
        yield meiju
