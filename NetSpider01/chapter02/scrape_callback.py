'''
Created on Jun 12, 2018

@author: xiongan2
'''
import re
import csv
import lxml.html
from chapter02.link_crawler import link_crawler


FIELDS = ('area', 'population', 'iso', 'country', 'capital', 'continent', 'tld', 'currency_code', 'currency_name', \
           'phone', 'postal_code_format', 'postal_code_regex', 'languages', 'neighbours')


def scrape_callback(url, html):
    print('scrape_callback')
    if re.search('/view/', url):
        tree = lxml.html.fromstring(html)
        row = [tree.cssselect('table > tr#places_{}__row > td.w2p_fw'.format(field))[0].text_content() for field in FIELDS]
        print(url, row)
        
class ScrapeCallback:
    def __init__(self):
        self.writer=csv.writer(open('countries.csv', 'w'))
        self.fields = ('area', 'population', 'iso', 'country', 'capital', 'continent', 'tld', 'currency_code', \
                       'currency_name', 'phone', 'postal_code_format', 'postal_code_regex', 'languages', 'neighbours')
        self.writer.writerow(self.fields)
    
    def __call__(self, url, html):
        if re.search('/view/', url):
            tree=lxml.html.fromstring(html)
            row=[]
            for field in self.fields:
                row.append(tree.cssselect('table > tr#places_{}__row > td.w2p_fw'.format(field))[0].text_content())
            self.writer.writerow(row)
        
#link_crawler('http://example.webscraping.com/', '(.*?)/(index|view)', scrape_callback=scrape_callback)
link_crawler('http://example.webscraping.com/', '(.*?)/(index|view)', scrape_callback=ScrapeCallback())