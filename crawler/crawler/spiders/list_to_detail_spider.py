import scrapy
from crawler.items import ArticleItem
from datetime import datetime
from crawler.models.article import Article
from crawler.utils.hash import create_url_hash
from urllib.parse import urlparse


class ListToDetailSpider(scrapy.Spider):

    name = "list_to_detail"

    start_urls = [
        "https://quotes.toscrape.com/"
    ]

    def parse(self, response):
        url = response.url
        self.logger.info("url: %s", url)
        self.logger.info("response status: %s", response.status)

        links = response.css(
            "small.author + a::attr(href)"
        ).getall()
        self.logger.info("number of links: %s", len(links))

        

        for link in set(links):

            yield response.follow(
                link,
                callback=self.parse_author
            )
        next_page = response.css(
            "li.next a::attr(href)"
        ).get()
        
        if next_page:
            self.logger.info("next page: %s", next_page)
            yield response.follow(
                next_page,
                callback = self.parse
            )

    def parse_author(self, response):
        self.logger.info("author url: %s", response.url)

        title = response.css(
            "h3.author-title::text"
        ).get()
        content = response.css(
            "div.author-description::text"
        ).get()
        author = response.css(
            "h3.author-title::text"
        ).get()
        category = response.css(
            "h3.author-title::text"
        ).get()
        article = Article(
            url = response.url,
            url_hash = create_url_hash(response.url),
            title = title.strip() if title else "",
            content = content.strip() if content else "",
            author = author.strip() if author else "",
            category = category.strip() if category else "",
            source = urlparse(response.url).netloc,
        
            crawled_at = datetime.now()
        )
        yield ArticleItem(
    **article.model_dump()
)