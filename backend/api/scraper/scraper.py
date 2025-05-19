import queue
import time
from concurrent.futures import ThreadPoolExecutor

import article_sources as asrc
from agent import RequestsAgent
from article import ArticleRepository
from article_scrapers import get_scraper
from driver import PROXY_OPTIONS

"""class MockSource(ArticleSource):

    def __init__(self, urls) -> None:
        self.urls = urls

    def __iter__(self):
        for url in self.urls:
            yield url"""


def main():
    repo = ArticleRepository("../data/articles")
    agent = RequestsAgent(proxy_config=PROXY_OPTIONS)

    def all_sources():
        # s = [asrc.OrigoSource, asrc.TelexSource, asrc.HvgSource, asrc.IndexSource, asrc.VGSource]
        s = [asrc.OrigoSource]
        for si in s:
            yield lambda i: si(agent, offset=i, max_index=i + 1, already_proposed=repo.fetched_urls)

    """class MockRepo:
        def save_article(self, article):
            print(f"Saving article: {article.title}")

    repo = MockRepo()"""
    """urls = [
        "https://www.origo.hu//itthon/2024/02/alapjogokert-kozpont-politikai-abuzus-balrol",
        "https://www.origo.hu//nagyvilag/2024/02/lemeszarolt-a-csaladjat-egy-kaliforniai-ferfi",
        "https://www.origo.hu//teve/2024/02/uj-baratja-van-gaspar-evelinnek-kep"
    ]
    source = MockSource(urls)"""

    buffer = queue.Queue()
    pages = queue.Queue()
    for i in range(0, 10):
        pages.put(i)

    def produce():
        while not pages.empty():
            page = pages.get()
            for source in all_sources():
                for url in source(page):
                    print(f"Produced {url}")
                    buffer.put(url)

        print("DONE")

    def consume():
        while True:  # buffer.empty():
            url = buffer.get()
            try:
                scraper = get_scraper(url)()
                artice = scraper.scrape(agent.fetch(url))
                repo.save_article(artice)
            except Exception as e:
                print(f"Error: {url}\n{e}")

    with ThreadPoolExecutor(max_workers=20) as executor:
        for _ in range(5):
            print("submitting produce")
            executor.submit(produce)
        while buffer.empty():
            time.sleep(0.1)
        for _ in range(15):
            print("submitting consume")
            executor.submit(consume)


if __name__ == "__main__":
    main()