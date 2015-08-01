import scrapy
from scraper.items import AppItem
import urlparse

class DescriptionScraper(scrapy.Spider):
    name = "dscrape"
    def __init__(self, category=""):
        self.category=category
        self.start_urls = [
            "https://play.google.com/store/apps/category/" + self.category.upper() + "/collection/topselling_paid",
            "https://play.google.com/store/apps/category/" + self.category.upper() + "/collection/topselling_free"
        ]
        self.f = open('../corpus/corpus_' + self.category.lower() + '.txt', 'w')
        self.urls_parsed = 0
        allowed_domains = ["play.google.com"]

    def parse(self, response):
        for href in response.xpath('//a[contains(@class, "title")][contains(@href, "/store/apps/details")]/@href'):
            url = urlparse.urljoin(response.url, href.extract())
            print url
            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        for sel in response.xpath('//div[contains(@class, "id-app-orig-desc")]'):
            item = AppItem()
            item['desc'] = sel.xpath('text()').extract()[0]
            for p in sel.xpath('.//p'):
                item['desc'] += p.extract()
            print item['desc']
            try: 
                self.f.write(item['desc'] + '\n')
            except:
                continue
        self.urls_parsed += 1
        if self.urls_parsed > 1:
            self.f.close()
