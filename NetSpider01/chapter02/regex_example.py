'''
Created on Jun 9, 2018

@author: xiongan2
'''
import re
import urllib.request

def scrape(html):
    html=html.decode('utf-8')
    pattern='<tr id="places_area__row">.*?<td\s*class=["\']w2p_fw["\']>(.*?)</td>'
    pattern2='<a href="/places/default/index">(.*?)</a>'
    area=re.findall(pattern2, html)[1]
    return area

html=urllib.request.urlopen('http://example.webscraping.com/view/United-Kingdom-239').read()
print(scrape(html))