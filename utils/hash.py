import hashlib


def create_url_hash(url: str) -> str:
    return hashlib.sha256(
        url.encode("utf-8")
    ).hexdigest()