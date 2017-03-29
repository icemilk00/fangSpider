
import scrapy
from fang.items import FangItem
from scrapy.selector import HtmlXPathSelector
from scrapy.selector import Selector
from scrapy.spider import BaseSpider
from scrapy.http import Request

class FangSpider(scrapy.spiders.Spider):

	name = 'fangSpider'
	allowed_domains = ["fangjia.fang.com"]

	start_urls = ["http://fangjia.fang.com"]

	def parse(self, response):

		print('url = %s' % response.url)
		baseUrl = response.url

		for sel in response.xpath('//div[@class = "linker gray6"][1]/a'):

			title = sel.xpath('strong/text()').extract()[0]
			url = baseUrl + sel.xpath('@href').extract()[0]
			print('a = %s, url = %s' % (title, url))

			yield Request(url, callback = self.parse_url)




	def parse_url(self, response):

		sel = Selector(response)

		fangItem = FangItem()

		fangItem['title'] = sel.xpath('//div[@class = "price-info "]/dl/dt/p/text()').extract()[0].strip()
		fangItem['cityName'] = sel.xpath('//div[@class = "price-info "]/dl/dt/h3/text()').extract()[0].strip()
		fangItem['currentMonthPriceTitle'] = sel.xpath('//div[@class = "price-info "]/dl/dd[1]/p/text()').extract()[0].strip()
		fangItem['currentMonthPrice'] = sel.xpath('//div[@class = "price-info "]/dl/dd[1]/div[@class = "h-rate"]/h3/text()').extract()[0].strip()
		fangItem['rateNum'] = sel.xpath('//div[@class = "price-info "]/dl/dd[1]//div[@class = "rate-num"]/span/text()').extract()[0].strip()
		fangItem['onSellNum'] = sel.xpath('//div[@class = "price-info "]/dl/dd[2]/h3/text()').extract()[0].strip()
		fangItem['lastMonthSellNumTitle'] = sel.xpath('//div[@class = "price-info "]/dl/dd[3]/p/text()').extract()[0].strip()
		fangItem['lastMonthSellNum'] = sel.xpath('//div[@class = "price-info "]/dl/dd[3]/h3/text()').extract()[0].strip()
		fangItem['url'] = response.url

		yield fangItem

