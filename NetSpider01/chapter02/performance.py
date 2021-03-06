'''
Created on Jun 10, 2018

@author: xiongan2
'''
import csv
import time
import urllib.request
import re
import timeit
from bs4 import BeautifulSoup
import lxml.html

FIELDS=('area', 'population', 'iso', 'country', 'capital', 'continent', 'tld', 'currency_code', \
        'currency_name', 'phone', 'postal_code_format', 'postal_code_regex', 'languages', 'neighbours')

def regex_scraper(html):
    results={}
    if html is not None:
        html=html.decode('utf-8')
    for field in FIELDS:
        print(field)
        results[field]=re.search('<a href="/places/default/index">(.*?)</a>', html).groups()[0]
    return results

def beautiful_soup_scraper(html):
    soup=BeautifulSoup(html,'html.parser')
    results={}
    for  field in FIELDS:
        results[field]=soup.find('table').find('tr', id='places_{}__row'.format(field)).find('td',class_='w2p_Fw').text
    return results

def lxml_scraper(html):
    tree=lxml.html.fromstring(html)
    results={}
    for  field in FIELDS:
        results[field] = tree.cssselect('table > tr#places_{}__row > td.w2p_fw'.format(field))[0].text_content()
    return results

def main():
    times = {}
    html=urllib.request.urlopen('http://example.webscraping.com/view/United-Kingdom-239').read()
    NUM_ITERATIONS = 1000 # number of times to test each scraper
    for name, scraper in ('Regular expressions', regex_scraper), ('Beautiful Soup', beautiful_soup_scraper), ('Lxml', lxml_scraper):
        times[name]=[]
        # record start time of scrape
        start=time.time()
        for i in range(NUM_ITERATIONS):
            if scraper==regex_scraper:
                # the regular expression module will cache results
                # so need to purge this cache for meaningful timings
                re.purge()
            result = scraper(html)
            
            # check scraped result is as expected
            # assert(result['area']=='244,820 square kilometres')
            times[name].append(time.time() - start)
        # record end time of scrape and output the total
        end = time.time()
        print('{}: {:.2f} seconds'.format(name, end - start))
        
    writer = csv.writer(open('times.csv', 'w'))
    header = sorted(times.keys())
    writer.writerow(header)
    for row in zip(*[times[scraper] for scraper in header]):
        writer.writerow(row)

if __name__ == '__main__':    
    main()
