# -*- coding: utf-8 -*-
import scrapy
from MyProject.items import Tencent

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = []
    for i in range(0,20,10):
        url = 'https://hr.tencent.com/position.php?lid=&tid=&keywords=python&start={}#a'.format(i)
        start_urls.append(url)

    def parse(self, response):
        print(response.body.decode('utf-8'))
        all = response.xpath('//table[@class="tablelist"]//tr')[1:-1]
        for i in all:
            tencent = Tencent()
            zw = i.xpath('./td[1]/a/text()').extract()[0]
            lb = i.xpath('./td[2]/text()').extract()[0]
            rs = i.xpath('./td[3]/text()').extract()[0]
            dd = i.xpath('./td[4]/text()').extract()[0]
            sj = i.xpath('./td[5]/text()').extract()[0]
            tz = i.xpath('./td[1]/a/@href').extract()[0]
            url = response.urljoin(tz)
            tencent['zw'] = zw
            tencent['lb'] = lb
            tencent['rs'] = rs
            tencent['dd'] = dd
            tencent['sj'] = sj
            tencent['url'] = url
            yield scrapy.Request(url = url,callback = self.detail,meta = {'tencent':tencent},dont_filter = False)
    def detail(self,response):
        tencent = response.meta['tencent']
        xq = response.xpath('//ul[@class="squareli"]')
        xq1 = xq[0].xpath('.//text()').extract()
        xq2 = xq[1].xpath('.//text()').extract()
        tencent['xq1'] = xq1
        tencent['xq2'] = xq2
        yield tencent

