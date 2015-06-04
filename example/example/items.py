# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ExampleItem(scrapy.Item):
	title = scrapy.Field()
	desc = scrapy.Field()
	hlink = scrapy.Field()
	
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
