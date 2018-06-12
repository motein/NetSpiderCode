'''
Created on Jun 13, 2018

@author: Xor
'''
import time
from chapter03.common import time_elapse
from chapter03.link_crawler import link_crawler

@time_elapse
def test_again(x):
    time.sleep(x)
    link_crawler('http://example.webscraping.com', '(.*?)/(index|view)', delay=0, num_retries=1, max_depth=1, user_agent='GoodCrawler')

test_again(1)