'''
Created on Jun 15, 2018

@author: Xor
'''
from chapter03.mongo_cache import MongoCache
from chapter04.alexa_cb import AlexaCallback
from chapter03.link_crawler import link_crawler

def main():
    scrape_callback = AlexaCallback()
    cache = MongoCache()
    #cache.clear()
    link_crawler(seed_url=scrape_callback.seed_url, user_agent='GoodCrawler', scrape_callback=scrape_callback, cache=cache, ignore_robots=True)
    
main()