# -*- coding: utf-8 -*-
import scrapy
import re
from urlparse import urlparse,parse_qs
from scrapy.selector import HtmlXPathSelector
from scrapy.loader import ItemLoader
from mynavi.items import CompanyItem, SeminarItem
from scrapy.contrib.loader.processor import Join, MapCompose, TakeFirst


class SeminarSpider(scrapy.Spider):
	name = "seminar"
	allowed_domains = ["job.mynavi.jp"]
	seminar_list_xpath = '//table[@class="tableSeminar"]/tbody/tr'

	re_loc = re.compile(r'mycom_loc\|(\d+)\/(\d+)\/(\d+\.\d+)\,(\d+)\/(\d+)\/(\d+\.\d+)')

	def start_requests(self):
		f = open('mynavi/spiders/test.txt','r')
		companyID = f.readline()
		IDList = companyID.split(',')
		for id in IDList:
			url = "http://job.mynavi.jp/17/pc/corpinfo/displaySeminarList/index?corpId="+id
			yield scrapy.Request(url, self.parse)

	def parse(self, response):
		match = re.search('/displaySeminarList/',response.url)

		if match:
			urls = response.xpath('//div[@class="internList splitEntry"]//@href').extract()
			for url in urls:
				url = response.urljoin(url)
				yield scrapy.Request(url, self.parse)
		else:
			table = response.xpath(self.seminar_list_xpath)
			corpId = parse_qs(urlparse(response.url).query)['corpId']
			for index,semi in enumerate(table):
				loader = ItemLoader(SeminarItem(),semi)
				loader.default_input_processor = MapCompose(unicode.strip)
				loader.default_output_processor = Join()
				loader.add_value('companyid',corpId)
				loader.add_xpath('name','//div[@id="headerWrap"]//h3/text()')
				loader.add_xpath('date','.//td[@class="date"]/text()',re='\d+\/\d+\/\d+')
				loader.add_xpath('time','.//td[@class="time"]/text()')
				loader.add_xpath('area','.//td[@class="area"]/text()')
				loader.add_xpath('place','.//td[@class="place"]/text()')
				loader.add_xpath('loc_n','.//td[@class="place"]//a', re='mycom_loc\|(\d+\/\d+\/\d+\.\d+)\,\d+\/\d+\/\d+\.\d+')
				loader.add_xpath('loc_e','.//td[@class="place"]//a', re='mycom_loc\|\d+\/\d+\/\d+\.\d+\,(\d+\/\d+\/\d+\.\d+)')
				loader.add_xpath('target','.//td[@class="target"]/text()')
				yield loader.load_item()