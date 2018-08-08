# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FendiParserItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    brand = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()
    size = scrapy.Field()
    images = scrapy.Field()
