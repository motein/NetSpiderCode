'''
Created on Jun 8, 2018

@author: xiongan2
'''
# -*- coding: utf-8 -*-

import re
from time import sleep
from chapter01.common import download3

def crawl_sitemap(url):
    # download the sitemap file
    sitemap=download3(url).decode('utf-8')
    # extract the sitemap links
    pattern="<loc>(.*?)</loc>"
    links=re.findall(pattern, sitemap)
    print(len(links))
    # download each link
    for link in links:
        html=download3(link)
        sleep(1) # sleep or too many requests
        # scrape html here
        # ...

if __name__ == '__main__':        
    crawl_sitemap('http://example.webscraping.com/sitemap.xml')
