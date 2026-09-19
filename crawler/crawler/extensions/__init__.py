from scrapy import signals
class StartExtiension:
    @classmethod
    def from_crawler(cls, crawler):
        extiension = cls()
        crawler.signals.connect(
            extiension.spider_closed,
            signal = signals.spider_closed
        )
        return extiension
    def spider_closed(self, spider):
        starts = spider.crawler.stats.get_stats()
        spider.logger.info("="*50)
        spider.logger.info("" \
        "response count: %s",
        starts.get("downloader/response_count",0))
        spider.logger.info("" \
        "request count: %s",
        starts.get("downloader/request_count",0))
        spider.logger.info("" \
        "item scraped count: %s",
        starts.get("item_scraped_count",0))
        spider.logger.info("" \
        "item dropped count: %s",
        starts.get("item_dropped_count",0))
        spider.logger.info("" \
        "retried count: %s",
        starts.get("retry/count",0))