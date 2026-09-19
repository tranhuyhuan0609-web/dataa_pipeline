import scrapy
class EXAMPLESpider(scrapy.Spider):
    name = "example"
    start_urls = [
        "https://quotes.toscrape.com/"
    ]
    def parse(self, response):
        # title = response.css("title::text").get()
        for quote in response.css("div.quote"):
            text = quote.css("span.text::text").get()
            author = quote.css("small.author::text").get()
            tag = quote.css("div.tags a.tag::text").getall()
            yield {
                "text": text,
                "author": author,
                "tag": tag
            }