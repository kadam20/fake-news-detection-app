import importlib
import pkgutil
from abc import abstractmethod

import article_scrapers
from agent import FetchResult
from article import Article
from utils import get_host_from_url

_REGISTERED_SCRAPERS = {}


class ArticleScraper:
    @abstractmethod
    def scrape(self, result: FetchResult) -> Article:
        raise NotImplementedError()


class register_scraper:
    def __init__(self, domain: str):
        self.domain = domain

    def __call__(self, scraper):
        print(f"Registering scraper: {scraper.__name__} for {self.domain}")
        assert self.domain not in _REGISTERED_SCRAPERS
        _REGISTERED_SCRAPERS[self.domain] = scraper
        return scraper


def get_scraper(url: str) -> ArticleScraper:
    # extract domain
    domain = get_host_from_url(url)
    s = _REGISTERED_SCRAPERS[domain]
    return s


# import all scrapers from the module automatically
def _import_all_scrapers():
    print("Importing all sources")
    for _, name, _ in pkgutil.iter_modules(article_scrapers.__path__):
        importlib.import_module(f"article_scrapers.{name}")


_import_all_scrapers()