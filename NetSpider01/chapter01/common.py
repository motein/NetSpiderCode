'''
Created on Jun 8, 2018

@author: xiongan2
'''
import builtwith
import whois
import urllib
import urllib.request
import urllib.parse
from future.backports.urllib.parse import urlparse

def download1(url):
    return urllib.request.urlopen(url).read()

def download2(url):
    print('Downloading:', url)
    try:
        html=urllib.request.urlopen(url).read()
    except urllib.error.URLError as e:
        print('Downloading error:', e.reason)
        html=None
    return html

def download3(url, num_retries=2):
    print('Downloading:', url)
    try:
        html=urllib.request.urlopen(url).read()
    except urllib.error.URLError as e:
        print('Downloading error:', e.reason)
        html=None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download3(url, num_retries-1) # recursively retry 5xx HTTP errors
    return html

def download4(url, user_agent='wswp', num_retries=2):
    print('Downloading:', url)
    headers={'User-agent':user_agent}
    request=urllib.request.Request(url,headers=headers)
    try:
        html=urllib.request.urlopen(request).read()
    except urllib.error.URLError as e:
        print('Downloading error:', e.reason)
        html=None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download4(url, user_agent, num_retries-1) # recursively retry 5xx HTTP errors
    return html

def download5(url, user_agent='wswp', proxy=None, num_retries=2):
    print('Downloading:', url)
    headers={'User-agent':user_agent}
    request=urllib.request.Request(url,headers=headers)
    opener=urllib.request.build_opener()
    if opener:
        proxy_params={urlparse(url).scheme:proxy}
        opener.add_handler(urllib.request.ProxyHandler(proxy_params))
    try:
        html=opener.open(request).read()
    except urllib.error.URLError as e:
        print('Downloading error:', e.reason)
        html=None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download4(url, user_agent, proxy, num_retries-1) # recursively retry 5xx HTTP errors
    return html

#print(builtwith.parse('http://example.webscraping.com'))
#print(whois.whois('appspot.com'))
print(download3('http://httpstat.us/500'))