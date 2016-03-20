# -*- coding: utf-8 -*-
import scrapy
import re
from urlparse import urlparse,parse_qs
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from mynavi.items import CompanyItem, SeminarItem

class SeminarSpider(scrapy.Spider):
	name = "seminar"
	allowed_domains = ["job.mynavi.jp"]
	seminar_list_xpath = '//table[@class="tableSeminar"]/tbody/tr'

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
			print table
			for index,semi in enumerate(table):
				print index
				print semi.xpath('.//td[@class="date"]/text()').extract()
    		return