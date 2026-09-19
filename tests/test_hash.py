from crawler.crawler.utils.hash import create_url_hash
def test_create_url_hash():
    url = "https://example.com/article/123"
    url_hash_1 = create_url_hash(url)
    url_hash_2 = create_url_hash(url)
    assert url_hash_1 == url_hash_2