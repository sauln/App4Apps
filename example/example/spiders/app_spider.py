import scrapy
from example.items import AppItem

class AppSpider(scrapy.Spider):
    name = "apper"
    allowed_domains = ["play.google.com"]
    start_urls = ["https://play.google.com/store/apps/category/FINANCE"]
	
    def parse(self, response):
        for sel in response.xpath('//*[contains(@class, "description")]'):
            item = AppItem()
            item['desc'] = (sel.xpath('text()').extract()

            print item['desc']
