'''
Created on Jun 15, 2018

@author: Xor
'''
from chapter03.mongo_cache import MongoCache
from chapter04.alexa_cb import AlexaCallback
from chapter04.crawler import crawler

def main():
    scrape_callback = AlexaCallback()
    cache = MongoCache()
    #cache.clear()
    crawler(scrape_callback.seed_url, scrape_callback=scrape_callback, cache=cache, timeout=10, ignore_robots=True)