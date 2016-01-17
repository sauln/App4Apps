import scrapy
from scraper.items import AppItem
import urlparse

class DescriptionScraper(scrapy.Spider):
    name = "dscrape"
    allowed_domains = ["play.google.com"]
    def __init__(self, category=""):
        self.category=category
        self.start_urls = [
            "https://play.google.com/store/apps/category/" + self.category.upper() + "/collection/topselling_paid",
            "https://play.google.com/store/apps/category/" + self.category.upper() + "/collection/topselling_free"
        ]
        self.f = open('../corpus/corpus_' + self.category.lower() + '.txt', 'w')


    def parse(self, response):
        for href in response.xpath('//a[contains(@class, "title")][contains(@href, "/store/apps/details")]/@href'):
            url = urlparse.urljoin(response.url, href.extract())
            print url
            yield scrapy.Request(url, callback=self.parse_dir_contents)
        #self.f.close()

    def parse_dir_contents(self, response):
        for sel in response.xpath('//div[contains(@class, "id-app-orig-desc")]'):
            item = AppItem()
            if sel.xpath('text()').extract():
                item['desc'] = sel.xpath('text()').extract()[0] + '\n'
                for p in sel.xpath('.//p'):
                    item['desc'] += p.extract() + '\n'
                print item['desc']
                try:
                    self.f.write(item['desc'] + '\n')
                except:
                    item['desc'] = replace_bad_characters(item['desc'])
                    self.f.write(item['desc'] + '\n')
                    continue

def replace_bad_characters(string):
    string = string.replace(u'\u2019', '')
    string = string.replace(u'\u014d', '')
    string = string.replace(u'\xea', '')
    string = string.replace(u'\u25ba', '')
    string = string.replace(u'\xe7', '')
    string = string.replace(u'\u2018', '')
    string = string.replace(u'\u2003', '')
    string = string.replace(u'\u2606', '')
    string = string.replace(u'\xa5', '')
    string = string.replace(u'\u2756', '')
    string = string.replace(u'\u25ab', '')
    string = string.replace(u'\xf1', '')
    string = string.replace(u'\u25a0', '')
    string = string.replace(u'\xe9', '')
    string = string.replace(u'\u2260', '')
    string = string.replace(u'\u9322', '')
    string = string.replace(u'\u2122', '')
    string = string.replace(u'\u2713', '')
    string = string.replace(u'\xae', '')
    string = string.replace(u'\u2022', '')
    string = string.replace(u'\u2013', '')
    string = string.replace(u'\xa9', '')
    string = string.replace(u'\xa0', '')
    string = string.replace(u'\u2014', '')
    string = string.replace(u'\u2028', '')
    string = string.replace(u'\u2714', '')
    string = string.replace(u'\u201c', '')
    string = string.replace(u'\u2666', '')
    string = string.replace(u'\u201d', '')
    string = string.replace(u'\u2605', '')
    string = string.replace(u'\u203b', '')
    string = string.replace(u'\xb7', '')
    string = string.replace(u'\u2026', '')
    string = string.replace(u'\u2033', '')
    string = string.replace(u'\xb1', '')
    string = string.replace(u'\u20ac', '')
    string = string.replace(u'\u2120', '')
    string = string.replace(u'\u4e21', '')
    string = string.replace(u'\xa3', '')
    string = string.replace(u'\u25cf', '')
    string = string.replace(u'\u20a9', '')
    string = string.replace(u'\xfa', '')
    string = string.replace(u'\xe2', '')
    return string
