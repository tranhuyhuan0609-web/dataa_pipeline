import scrapy


class ListToDetailSpider(scrapy.Spider):

    name = "list_to_detail1"

    start_urls = [
        "https://quotes.toscrape.com/"
    ]

    def parse(self, response):

        print("PARSE DA DUOC GOI")
        print("URL:", response.url)
        print("STATUS:", response.status)

        yield {
            "test": "HELLO"
        }