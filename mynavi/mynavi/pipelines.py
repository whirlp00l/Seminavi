# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
from sqlalchemy.orm import sessionmaker
from model import Company, Seminar, db_connect, create_deals_table
from items import CompanyItem, SeminarItem

class MynaviPipeline(object):
	def __init__(self):
		engine = db_connect()
		create_deals_table(engine)
		self.Session = sessionmaker(bind=engine)

	def process_item(self, item, spider):
		session = self.Session()
		if isinstance(item, SeminarItem):
			seminar = Seminar(**item)
			try:
				session.add(seminar)
				session.commit()
			except:
				session.rollback()
				raise
			finally:
				session.close()
			return item