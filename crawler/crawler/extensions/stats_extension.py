from scrapy import signals
import time


class StatsExtension:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    @classmethod
    def from_crawler(cls, crawler):

        extension = cls()
        crawler.signals.connect(
            extension.spider_opened,
            signal=signals.spider_opened
        )

        crawler.signals.connect(
            extension.spider_closed,
            signal=signals.spider_closed
        )

        return extension
    def spider_opened(self, spider):
        self.start_time = time.time()

    def spider_closed(self, spider):
        duration = time.time() - self.start_time

        stats = spider.crawler.stats.get_stats()

        spider.logger.info("=" * 50)
        spider.logger.info("CRAWL STATISTICS")
        spider.logger.info(
            "Requests: %s",
            stats.get("downloader/request_count", 0)
        )
        spider.logger.info(
            "Responses: %s",
            stats.get("downloader/response_count", 0)
        )
        spider.logger.info(
            "Items scraped: %s",
            stats.get("item_scraped_count", 0)
        )
        spider.logger.info(
            "Items dropped: %s",
            stats.get("item_dropped_count", 0)
        )
        spider.logger.info(
            "Retries: %s",
            stats.get("retry/count", 0)
        )
        spider.logger.info("" \
        "HTTP 200: %s",
            stats.get("downloader/response_status_count/200", 0)
        )
        spider.logger.info("" \
        "HTTP 404: %s",
            stats.get("downloader/response_status_count/404", 0))
        spider.logger.info("" \
        "HTTP 308: %s",
            stats.get("downloader/response_status_count/308", 0)
        )
        spider.logger.info("" \
        "Duration: %.2f seconds",
        duration)
        spider.logger.info("" \
        "duplicate count: %s",
        stats.get("dupefilter/filtered", 0))