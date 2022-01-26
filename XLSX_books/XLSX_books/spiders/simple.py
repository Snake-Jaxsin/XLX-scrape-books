import scrapy

class SimpleSpider(scrapy.Spider):
    name = 'simple'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):
        for s in response.css('.col-xs-6'):
            title = s.css('h3 a::attr(title)').get()
            price = s.css('p.price_color::text').get()[1:]
            stock = s.css('p.instock::text')[1:].get().strip()

            item = {}
            item['title'] = title
            item['price'] = price
            item['stock'] = stock

            yield item







