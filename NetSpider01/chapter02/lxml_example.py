'''
Created on Jun 10, 2018

@author: xiongan2
'''
import urllib.request
import lxml.html
import lxml.cssselect

def scrape(html):
    tree=lxml.html.fromstring(html)
    #print(lxml.html.tostring(tree))
    td=tree.cssselect('header#header > div.span12 > div.page-header')[0]
    area=td.text_content()
    return area

html=urllib.request.urlopen('http://example.webscraping.com/view/United-Kingdom-239').read()
print(scrape(html))