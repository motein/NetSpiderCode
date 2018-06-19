'''
Created on Jun 15, 2018

@author: xiongan2
'''
from chapter04.threaded_crawler import threaded_crawler
from chapter03.mongo_cache import MongoCache
from chapter04.alexa_cb import AlexaCallback


def main(max_threads):
    scrape_callback = AlexaCallback()
    cache = MongoCache()
    #cache.clear()
    threaded_crawler(scrape_callback.seed_url, scrape_callback=scrape_callback, cache=cache, max_threads=max_threads, timeout=10)

if __name__ == '__main__':   
    max_threads = int(20)
    main(max_threads)