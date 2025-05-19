from datetime import datetime

from agent import FetchResult
from article import Article

from .base import ArticleScraper, register_scraper


@register_scraper("cnn.com")
class CNNScraper(ArticleScraper):

    def scrape(self, result: FetchResult) -> Article:
        soup = result.content
        tags = soup.find("meta", attrs={"name": "keywords"})["content"].split(", ")
        author = soup.find("meta", attrs={"name": "author"})["content"]
        title = soup.find("meta", property="og:title")["content"]
        timestamp_str = soup.find("meta", property="og:updated_time")["content"]
        timestamp = datetime.strptime(timestamp_str.split(".")[0], "%Y-%m-%dT%H:%M:%S")

        article_content = soup.select_one(".article-content")
        images = list(map(lambda x: x["src"], article_content.select("img")))
        image_alts = list(map(lambda x: x["alt"] if "alt" in x else None, article_content.select("img")))
        body = article_content.text
        links = list(map(lambda x: x["href"], article_content.select("a")))

        return Article(
            domain="cnn.com",
            title=title,
            author=author,
            timestamp=timestamp,
            url=result.url,
            body=body,
            images=images,
            image_alts=image_alts,
            links=links,
            tags=tags,
            extra={},
        )