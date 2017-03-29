# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class FangPipeline(object):
	def __init__(self):
		print('__init__')
		self.file = open('./fang.json','wb')
		self.dataArray = []

	def  open_spider(self, spider):
		print('spider open  !!!!!!!!!!')

	def close_spider(self, spider):
		print('spider close  !!!!!!!!!!')
		line = json.dumps(self.dataArray)
		self.file.write(bytes(line, 'UTF-8'))

	def process_item(self, item, spider):

		self.dataArray.append(dict(item))

		return item
