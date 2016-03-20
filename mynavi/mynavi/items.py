# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class CompanyItem(scrapy.Item):
	url = scrapy.Field()
	detail = scrapy.Field()
	name = scrapy.Field()
	companyid = scrapy.Field()


class SeminarItem(scrapy.Item):
	companyid = scrapy.Field()
	name = scrapy.Field()
	date = scrapy.Field()
	time = scrapy.Field()
	place = scrapy.Field()
	target = scrapy.Field()
	submit = scrapy.Field()
