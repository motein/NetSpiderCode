'''
Created on Jun 19, 2018

@author: xiongan2
'''
from chapter03.downloader import Downloader
from selenium import webdriver
from lxml import html

def selenium_search():
    driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver')
    driver.get('http://example.webscraping.com/places/default/search')
    driver.find_element_by_id('search_term').send_keys('X')
    driver.execute_script("document.getElementById('page_size').options[1].text = '1000'");
    driver.find_element_by_id('search').click()
    driver.implicitly_wait(30)
    links = driver.find_elements_by_css_selector('#results a')
    countries = [link.text for link in links]
    driver.close()
    print(countries)

def get_dynamic():
    url='http://example.webscraping.com/dynamic'
    D=Downloader()
    content=D(url)
    #print(content.decode('utf-8'))
    tree=html.fromstring(content)
    print(tree.cssselect('#results')[0].text_content())

if __name__ == '__main__':
    #selenium_search()
    get_dynamic()