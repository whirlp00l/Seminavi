# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.contrib.loader.processor import Join, MapCompose, TakeFirst


def process_pos(value):
	value = value.split('/')
	value = float(value[0])+float(value[1])/60.0+float(value[2])/3600.0
	value = [unicode(value)]
	return value

class CompanyItem(scrapy.Item):
	url = scrapy.Field()
	detail = scrapy.Field()
	name = scrapy.Field()
	companyid = scrapy.Field()


class SeminarItem(scrapy.Item):
	companyid = scrapy.Field(
		input_processor=MapCompose(int),
		output_processor=TakeFirst(),
	)
	name = scrapy.Field()
	date = scrapy.Field()
	time = scrapy.Field()
	area = scrapy.Field()
	place = scrapy.Field()
	loc_n = scrapy.Field(
		input_processor=MapCompose(unicode.strip,process_pos),
		output_processor=Join(),
	)
	loc_e = scrapy.Field(
		input_processor=MapCompose(unicode.strip,process_pos),
		output_processor=Join(),
	)
	target = scrapy.Field()
	submit = scrapy.Field()
