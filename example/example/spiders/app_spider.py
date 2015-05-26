import scrapy

class AppSpider(scrapy.Spider):
	name = "apper"
	allowed_domains = ["play.google.com"]
	start_urls = ["http://www.play.google.com"]
	
	def parse(self, response):
		filename = response.url.split("/")[-2]
		with open(filename, 'wb') as f:
			f.write(response.body)