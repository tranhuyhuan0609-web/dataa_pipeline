import scrapy
class ErrorHandlingSpider(scrapy.Spider):
    name = "error_handling"

    start_urls = [
        "https://quotes.toscrape.com/",
        "https://quotes.toscrape.com/not_found"
    ]
    handle_httpstatus_list = [404]
    def parse(self, response):
        url = response.url
        http_status = response.status
        if http_status == 200:
            self.logger.info(f"Successfully scraped URL: {url}  ")
        elif http_status == 404:
            self.logger.warning(f"URL not found: {url}")
        else:
            self.logger.error(f"Error scraping URL: {url} with status code: {http_status}")