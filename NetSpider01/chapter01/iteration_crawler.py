'''
Created on Jun 8, 2018

@author: xiongan2
'''
import itertools
from time import sleep
from chapter01.common import download3

def iteration1():
    for page in itertools.count(1):
        url = 'http://example.webscraping.com/view/-%d' % page
        # url = 'http://example.webscraping.com/view/-{}'.format(page)
        html=download3(url)
        sleep(1)
        if html is None:
            # received an error trying to download this web page
            # so assume have reached the last country ID and can stop downloading
            break;
        else:
            # success - can scrape the result
            # ...
            pass

def iteration2():
    max_errors=5 # maximum number of consecutive download errors allowed
    num_errors=0 # current number of consecutive download errors
    for page in itertools.count(1):
        url = 'http://example.webscraping.com/view/-{}'.format(page)
        html=download3(url)
        sleep(1)
        if html is None:
            # received an error trying to download this web page
            num_errors+=1
            if num_errors == max_errors:
                # reached maximum amount of errors in a row so exit
                break
            # so assume have reached the last country ID and can stop downloading
        else:
            # success - can scrape the result
            # ...
            num_errors=0 # recount again
            
if __name__ == '__main__':
    iteration2()