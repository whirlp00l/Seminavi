# -*- coding: utf-8 -*-
import scrapy
import re

class SeminarSpider(scrapy.Spider):
	name = "seminar"
	allowed_domains = ["job.mynavi.jp"]

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
			self.parse_item(response)

	def parse_item(self, response):
		url = response.url
		title = response.xpath('//headerWrap//h3/text()').extract()
		date = response.xpath('//td[@class="date"]/text()').extract()
		time = response.xpath('//td[@class="time"]/text()').extract()
		place = response.xpath('//td[@class="place"]/text()').extract()
		target = response.xpath('//td[@class="area"]/text()').extract()
		submit = response.xpath('//td[@class="submit"]//@herf').extract()
