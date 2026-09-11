from datetime import datetime
from pydantic import BaseModel
class Article(BaseModel):
    url: str
    url_hash: str
    title: str
    content: str
    source: str
    category : str
    author : str
    published_at : datetime
    crawled_at: datetime