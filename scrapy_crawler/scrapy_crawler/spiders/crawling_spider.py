import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.item import Item, Field

class DocumentItem(Item):
    url = Field()
    html_content = Field()

class CrawlingSpider(CrawlSpider):
    name = 'crawling'
    allowed_domains = ['books.toscrape.com']
    start_urls = ["http://books.toscrape.com/"]
    max_pages = 10
    max_depth = 3

    rules = (
        Rule(LinkExtractor(allow='catalogue/category')),
        Rule(LinkExtractor(allow='catalogue', deny="category"), callback='parse_item'),
    )

    def __init__(self, *args, **kwargs):
        super(CrawlingSpider, self).__init__(*args, **kwargs)
        self.documents = []

    def parse_item(self, response):
        if response.meta.get('depth', 0) <= self.max_depth:
            item = DocumentItem()
            item['url'] = response.url
            item['html_content'] = response.text
            self.documents.append(response.text)
            yield item

    def parse(self, response):
        if len(response.meta.get('redirect_urls', [])) <= self.max_pages:
            return super().parse(response)
