from crawler.crawler.pipelines import DuplicateFilterPipeline
import pytest
from scrapy.exceptions import DropItem
def test_duplicate_filter_pipeline():
    item = {
        "url": "https://example.com/article1",
        "url_hash": "hash1",
    }
    pipeline = DuplicateFilterPipeline()
    result = pipeline.process_item(item, None)
    assert result == item
    with pytest.raises(DropItem):
        pipeline.process_item(item, None)