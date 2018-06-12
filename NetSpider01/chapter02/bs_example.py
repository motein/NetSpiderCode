'''
Created on Jun 10, 2018

@author: xiongan2
'''
import urllib.request
from bs4 import BeautifulSoup

def scrape(html):
    soup=BeautifulSoup(html, 'html.parser')
    tr=soup.find(attrs={'id':'header'}) # locate the area row
    # 'class' is a special python attribute so instead 'class_' is used
    td=tr.find(attrs={'class':'page-header'}) # locate the area tag
    area=td.text # extract the area contents from this tag
    return area

html=urllib.request.urlopen('http://example.webscraping.com/view/United-Kingdom-239').read()
print(scrape(html))