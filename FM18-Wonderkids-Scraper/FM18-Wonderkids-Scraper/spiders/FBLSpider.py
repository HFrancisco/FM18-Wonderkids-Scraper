# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector


class FBLSpider(scrapy.Spider):
    name = 'fblBot'

    def start_requests(self):
        urls = [
            'https://www.fmscout.com/a-football-manager-2018-wonderkids.html',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
 
    def parse(self, response):
        for row in response.xpath('//*[@id="dl"]/tbody/tr'):
            yield {
                'rating' : row.xpath('td[1]//text()').extract_first(),
                'name' : row.xpath('td[2]//text()').extract_first(),
                'age' : row.xpath('td[3]//text()').extract_first(),
                'position' : row.xpath('td[4]//text()').extract_first(),
                'club' : row.xpath('td[5]//text()').extract_first(),
                'wage' : row.xpath('td[6]//text()').extract_first(),
                'value' : row.xpath('td[7]//text()').extract_first(),
                'nation' : row.xpath('td[8]//img/@alt').extract_first(),
            }