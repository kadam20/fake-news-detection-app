from datetime import datetime

from agent import FetchResult
from article import Article

from .base import ArticleScraper, register_scraper


@register_scraper("nbc.com")
class NBCScraper(ArticleScraper):

    def scrape(self, result: FetchResult) -> Article:
        soup = result.content
        tags = soup.find("meta", attrs={"name": "keywords"})["content"].split(", ")
        author = soup.find("meta", attrs={"name": "author"})["content"]
        title = soup.find("meta", property="og:title")["content"]
        timestamp = datetime.fromisoformat(soup.find("meta", property="og:updated_time")["content"])

        current_post = soup.css.select(".current-post")[0]
        images = list(map(lambda x: x["src"], current_post.css.select("img")))
        image_alts = list(map(lambda x: x["alt"] if "alt" in x else None, current_post.css.select("img")))
        body = current_post.css.select(".text")[0].text
        links = list(map(lambda x: x["href"], current_post.css.select(".text a")))

        return Article(
            domain="nbc.com",
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