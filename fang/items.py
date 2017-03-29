# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FangItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	title = scrapy.Field()					#信息title
	cityName = scrapy.Field()				#城市名字
	currentMonthPriceTitle = scrapy.Field()	#当月均价title
	currentMonthPrice = scrapy.Field()		#当月均价
	rateNum = scrapy.Field()				#环比上月
	onSellNum = scrapy.Field()				#挂牌房源套
	lastMonthSellNumTitle = scrapy.Field()	#上月成交量title
	lastMonthSellNum = scrapy.Field()		#上月成交量
	url = scrapy.Field()					#来源

