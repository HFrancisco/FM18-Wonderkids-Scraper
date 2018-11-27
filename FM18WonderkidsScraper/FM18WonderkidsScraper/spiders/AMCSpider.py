# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector
from FM18WonderkidsScraper.items import Player


class AMCSpider(scrapy.Spider):
    name = 'amcBot'

    def start_requests(self):
        urls = [
            'https://www.fmscout.com/a-football-manager-2018-wonderkids.html',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
 
    #def parse(self, response):
    #    for row in response.xpath('//*[@id="amc"]/tbody/tr'):
    #        yield {
    #            'rating' : row.xpath('td[1]//text()').extract_first(),
    #            'name' : row.xpath('td[2]//text()').extract_first(),
    #            'age' : row.xpath('td[3]//text()').extract_first(),
    #            'position' : row.xpath('td[4]//text()').extract_first(),
    #            'club' : row.xpath('td[5]//text()').extract_first(),
    #            'wage' : row.xpath('td[6]//text()').extract_first(),
    #            'value' : row.xpath('td[7]//text()').extract_first(),
    #            'nation' : row.xpath('td[8]//img/@alt').extract_first(),
    #        }

    def parse(self, response):
        for row in response.xpath('//*[@id="amc"]/tbody/tr'):
            item = Player()

            item['rating'] = row.xpath('td[1]//text()').extract_first()
            item['name'] = row.xpath('td[2]//text()').extract_first()
            item['age'] = row.xpath('td[3]//text()').extract_first()
            item['position'] = row.xpath('td[4]//text()').extract_first()
            item['club'] = row.xpath('td[5]//text()').extract_first()
            item['wage'] = row.xpath('td[6]//text()').extract_first()
            item['value'] = row.xpath('td[7]//text()').extract_first()
            item['nation'] = row.xpath('td[8]//img/@alt').extract_first()

            yield item