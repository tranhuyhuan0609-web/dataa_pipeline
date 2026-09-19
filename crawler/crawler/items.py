# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# from dataclasses import dataclass


# @dataclass
# class CrawlerItem:
#     # define the fields for your item here like:
#     # name: str | None = None
#     pass
import scrapy


class ArticleItem(scrapy.Item):

    url = scrapy.Field()
    url_hash = scrapy.Field()

    title = scrapy.Field()
    content = scrapy.Field()

    source = scrapy.Field()
    author = scrapy.Field()
    category = scrapy.Field()

    published_at = scrapy.Field()
    crawled_at = scrapy.Field()