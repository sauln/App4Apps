import scrapy
from scraper.items import AppItem



class AppSpider(scrapy.Spider):
    name = "apper"
    allowed_domains = ["play.google.com"]

    def __init__(self, category=""):
        self.category=category
        self.start_urls = ["https://play.google.com/store/apps/category/" + category.upper() + "/collection/topselling_paid"]
    def parse(self, response):
        f = open('../corpus/corpus_' + self.category.lower() + '.txt', 'w')
        for sel in response.xpath('//*[contains(@class, "description")]'):
            item = AppItem()
            item['desc'] = sel.xpath('text()').extract()[0]
            print item['desc']
            try: 
                f.write(item['desc'] + '\n')
            except:
                continue
        
        f.close()
