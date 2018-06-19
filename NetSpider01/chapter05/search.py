'''
Created on Jun 19, 2018

@author: xiongan2
'''
import lxml.html
import json
import string
import csv
from chapter03.downloader import Downloader
from chapter03.mongo_cache import MongoCache

FIELDS = ('area', 'population', 'iso', 'country', 'capital', 'continent', 'tld', 'currency_code', 'currency_name', \
          'phone', 'postal_code_format', 'postal_code_regex', 'languages', 'neighbours')

def fail_search():
    D=Downloader()
    html=D('http://example.webscraping.com/search')
    tree=lxml.html.fromstring(html)
    tree.cssselect('div#results a')

def direct_download_ajax():
    D=Downloader()
    html=D('http://example.webscraping.com/ajax/')
    content=json.loads(html.decode('utf-8'))
    print(content)

# code cannot be executed, because the web has been rewritten.
def search1():
    template_url = 'http://example.webscraping.com/ajax/search.json?page={}&page_size=10&search_term={}'
    countries = set()
    download = Downloader(cache=MongoCache())

    for letter in string.ascii_lowercase:
        page = 0
        
        while True:
            url=template_url.format(page, letter)
            print("URL: ", url)
            html = download(url)
            try:
                ajax = json.loads(html)
            except ValueError as e:
                print(e)
                ajax = None
            else:
                for record in ajax['records']:
                    countries.add(record['country'])
            page += 1
            if ajax is None or page >= ajax['num_pages']:
                break
    
    open('countries.txt', 'w').write('\n'.join(sorted(countries)))
    
def search2():
    writer = csv.writer(open('countries.csv', 'w'))
    D = Downloader()
    html = D('http://example.webscraping.com/places/default/search?page=0&page_size=1000&search_term=.')
    print(html.decode('utf-8'))
    ajax = json.loads(html)
    for record in ajax['records']:
        writer.writerow([record['country']])
  
if __name__ == '__main__':
    #fail_search()
    #direct_download_ajax()
    search1()
else:
    print(__name__)