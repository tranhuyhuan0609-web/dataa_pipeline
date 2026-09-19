from datetime import datetime

from crawler.crawler.models import article
from crawler.crawler.models.article import Article
from crawler.crawler.utils.hash import create_url_hash


url = "https://example.com/article/123"
def test_article_model():  

    article = Article(
    url=url,
    url_hash=create_url_hash(url),
    title="AI is changing technology",
    content="Artificial intelligence is developing rapidly.",
    source="example",
    author="John Doe",
    category="technology",
    published_at=datetime(2023, 10, 1, 12, 0, 0),
    crawled_at=datetime.now()
)
    assert article.url == url
    assert article.title == "AI is changing technology"
    