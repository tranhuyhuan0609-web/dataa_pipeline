# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter


# class CrawlerPipeline:
#     def process_item(self, item):
#         return item
import re
from datetime import datetime
from crawler.items import ArticleItem
from crawler.utils.hash import create_url_hash
from crawler.utils.datetime import parse_datetime
class CleaningItemPipeline:
    def process_item(self, item, spider):
        if item.get("title"):
            item["title"] = self.cleaned_data(item["title"])
        if item.get("content"):
            item["content"] = self.cleaned_data(item["content"])
        if item.get("author"):
            item["author"] = self.cleaned_data(item["author"])
        if item.get("category"):
            item["category"] = self.cleaned_data(item["category"])
        if item.get("published_at"):
            item["published_at"] = parse_datetime(item["published_at"])
        if item.get("url"):
            
            item["url"] = item["url"].strip()
            item["url_hash"] = create_url_hash(item["url"])
        return item
    def cleaned_data(self, data):
        if isinstance(data, str):
            data = data.strip()
            data = re.sub(r"\s+", " ", data)
        return data
class ValidationItemPipeline:
    def process_item(self, item, spider):
        required_fields = ["title", "content", "url", "url_hash", "source",]
        for field in required_fields:
            value = item.get(field)
            if not value:
                spider.logger.warning(f"Missing required field '{field}' in item: {item}")
                raise DropItem(f"Missing required field '{field}' in item: {item}")
            if isinstance(value, str) and not value.strip():
                    spider.logger.warning(f"Empty required field '{field}' in item: {item}")
                    raise DropItem(f"Empty required field '{field}' in item: {item}")
            crawler_at = item.get("crawled_at")
            published_at = item.get("published_at")
            if not isinstance(crawler_at,datetime):
                spider.logger.warning(f"Invalid 'crawled_at' field in item: {item}")
                raise DropItem(f"Invalid 'crawled_at' field in item: {item}")
            if published_at is not None:
                if isinstance(published_at,datetime):
                    if published_at > crawler_at:
                        spider.logger.warning(f"'published_at' field is in the future compared to 'crawled_at' in item: {item}")
                        raise DropItem(f"'published_at' field is in the future compared to 'crawled_at' in item: {item}")
                else :
                    spider.logger.warning(f"Invalid 'published_at' field in item: {item}")
                    raise DropItem(f"Invalid 'published_at' field in item: {item}")
        return item
from scrapy.exceptions import DropItem
class DuplicateFilterPipeline:
    def __init__(self):
        self.seen_urls = set()
    def process_item(self, item, spider):
        url_hash = item.get("url_hash")
        if not url_hash:
            spider.logger.warning(f"Missing 'url_hash' in item: {item}")
            raise DropItem(f"Missing 'url_hash' in item: {item}")
        if url_hash in self.seen_urls:
           
            if spider:

               spider.logger.warning(f"Duplicate item found: {item}")
            raise DropItem(f"Duplicate item found: {item}")
        else:
            self.seen_urls.add(url_hash)
            return item


