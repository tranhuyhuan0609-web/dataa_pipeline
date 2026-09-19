import scrapy
class PaginationSpider(scrapy.Spider):
    name = 'pagination_spider'
    start_urls = ['https://quotes.toscrape.com/']
    def parse(self,response):
        print(response.url)
        quote = response.css('div.quote')
        print(len(quote))
        next_page = response.css('li.next a::attr(href)').get()
        print(next_page)
        yield response.follow(
            next_page,
            callback=self.parse
        )