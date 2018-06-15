'''
Created on Jun 14, 2018

@author: Xor
'''
import csv
from zipfile import ZipFile
from io import BytesIO, TextIOWrapper
from chapter03.mongo_cache import MongoCache

# return all links in a list
class AlexaCallback: 
    def __init__(self, max_urls=1000):
        self.max_urls = max_urls
        self.seed_url = 'http://s3.amazonaws.com/alexa-static/top-1m.csv.zip'

    def __call__(self, url, html):
        if url == self.seed_url:
            urls = []
            cache = MongoCache()
            with ZipFile(BytesIO(html)) as zf:
                csv_filename = zf.namelist()[0]
                mess=zf.open(csv_filename, 'r')
                mess=TextIOWrapper(mess)
                for _, website in csv.reader(mess):
                    print(website)
                    if 'http://' + website not in cache:
                        urls.append('http://' + website)
                        if len(urls) == self.max_urls:
                            break
            return urls