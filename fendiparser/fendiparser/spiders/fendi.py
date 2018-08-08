import scrapy
from ..items import FendiParserItem

class FendiSpider(scrapy.Spider):
    name = "fendi"
    start_urls = ["https://www.fendi.com/us/woman/bags",
                  "https://www.fendi.com/us/woman/shoes",
                  "https://www.fendi.com/us/man/bags",
                  "https://www.fendi.com/us/man/shoes",
                  ]

    def parse(self, response): # parsing main page
        for href in response.xpath('//div[contains(@class, "products")]/div[contains(@class, "listing")]/'
                                   'div[contains(@class, "product-card")]/'
                                   'div[@class="inner"]/div[@class="meta"]/div[@class="front"]/'
                                   'div[@class="name"]/a/@href').extract():
            yield scrapy.Request('https://www.fendi.com'+href, callback=self.parse_article)

    def parse_article(self, response):
        item = FendiParserItem()
        item['title'] = self.parse_title(response)
        item['price'] = self.parse_price(response)
        item['description'] = self.parse_description(response)
        item['images'] = self.parse_images(response)
        item['size'] = self.parse_size(response)


        yield item

    def parse_title(self, response):
        title = response.selector.xpath('//div[@class="product-info"]/'
                                        'div[@class="product-description"]/h1/text()').extract()
        return title

    def parse_price(self, response):
        price = response.selector.xpath('//div[@class="product-info"]/'
                                        'div[@class="product-description"]/div[contains(@class, "prices")]/'
                                        'span[@class="price "]/text()').extract()
        return price

    def parse_description(self, response):
        description = response.selector.xpath('//div[@class="product-tab"]/'
                                        'div[contains(@class, "tabcordion")]/div[@class="tab-content"]'
                                        '/div[contains(@class, "active")]/p/text()').extract()
        return description

    def parse_images(self, response):
        images = response.xpath('//img[@class="lazyload"]/@src').extract()
        return images

    def parse_size(self, response):
        size = response.selector.xpath('//div[@class="product-info"]/'
                                        'div[contains(@class, "product-form")]/form/div[@class="form-group"]/'
                                        'select[contains(@class, "form-control")]/option/text()').extract()
        return size
