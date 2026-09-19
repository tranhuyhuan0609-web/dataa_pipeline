from datetime import datetime
from pydantic import BaseModel
from typing import Optional
class Article(BaseModel):
    url: str
    url_hash: str
    title: str
    content: str
    source: str
    category : str
    author : str
    published_at : Optional[datetime] = None
    crawled_at: datetime