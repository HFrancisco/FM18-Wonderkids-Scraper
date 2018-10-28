# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Player(scrapy.Item):
    rating = scrapy.Field()
    name = scrapy.Field()
    age = scrapy.Field()
    position = scrapy.Field()
    club = scrapy.Field()
    wage = scrapy.Field()
    value = scrapy.Field()
    nation = scrapy.Field()