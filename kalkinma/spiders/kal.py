import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst
from kalkinma.items import Article


class KalSpider(scrapy.Spider):
    name = 'kal'
    allowed_domains = ['kalkinma.com.tr']
    start_urls = ['https://kalkinma.com.tr/bizi-taniyin/basin-odasi/bizden-haberler']

    def parse(self, response):
        links = response.xpath('//div[@class="c-news-box"]//a/@href').getall()
        yield from response.follow_all(links, self.parse_article)

    def parse_article(self, response):
        item = ItemLoader(Article())
        item.default_output_processor = TakeFirst()

        title = response.xpath('//div[@class="c-detail-gallery__title"]//text()').get()

        content = response.xpath('//div[@class="c-detail-gallery__text"]//text()').getall()
        content = "\n".join(content).strip()

        item.add_value('title', title)
        item.add_value('link', response.url)
        item.add_value('content', content)

        return item.load_item()
