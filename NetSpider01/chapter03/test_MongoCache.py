'''
Created on Jun 14, 2018

@author: xiongan2
'''
from chapter03.mongo_cache import MongoCache

cache=MongoCache()
result={'html':'wwww'}
url='url'
cache[url]=result
print(cache[url])