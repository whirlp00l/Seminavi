# -*- coding: utf-8 -*-
import scrapy



class SeminarSpider(scrapy.Spider):
	name = "seminar"
	allowed_domains = ["job.mynavi.jp"]

	def start_requests(self):
		f = open('mynavi/spiders/companyID.txt','r')
		companyID = f.readline()
		IDList = companyID.split(',')
		for id in IDList:
			url = "http://job.mynavi.jp/17/pc/corpinfo/displaySeminarList/index?corpId="+id
			yield scrapy.Request(url, self.parse)

	def parse(self, response):
		pass
