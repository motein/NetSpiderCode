'''
Created on Jun 15, 2018

@author: xiongan2
'''
import sys
from chapter04.process_crawler import process_crawler
from chapter03.mongo_cache import MongoCache
from chapter04.alexa_cb import AlexaCallback


def main(max_threads):
    scrape_callback = AlexaCallback()
    cache = MongoCache()
    cache.clear()
    process_crawler(scrape_callback.seed_url, scrape_callback=scrape_callback, cache=cache, max_threads=max_threads, timeout=10)
    
max_threads = int(4)
main(max_threads)