from datetime import datetime

from models.article import Article
from utils.hash import create_url_hash


url = "https://example.com/article/123"

article = Article(
    url=url,
    url_hash=create_url_hash(url),
    title="AI is changing technology",
    content="Artificial intelligence is developing rapidly.",
    source="example",
    crawled_at=datetime.now()
)

print(article)