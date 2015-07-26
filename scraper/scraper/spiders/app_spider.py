import scrapy
from scraper.items import AppItem



class AppSpider(scrapy.Spider):
    name = "apper"
    allowed_domains = ["play.google.com"]
    start_urls = ["https://play.google.com/store/apps/category/FINANCE/collection/topselling_paid"]
	
    def parse(self, response):
        f = open('../corpus/corpus.txt', 'w')
        for sel in response.xpath('//*[contains(@class, "description")]'):
            item = AppItem()
            item['desc'] = sel.xpath('text()').extract()[0]
            print item['desc']
            try: 
                f.write(item['desc'] + '\n')
            except:
                continue
        
        f.close()
