'''
Created on Jun 8, 2018

@author: xiongan2
'''
import re
import urllib.parse
import time
from time import sleep
from chapter01.common import download3
from datetime import datetime
from future.backports.urllib import robotparser
from queue import deque

def link_crawler1(seed_url, link_regex):
    """Craw from the given seed URL following links matched by link_regex
    """
    crawl_queue=[seed_url] # the queue of URL's to download
    while crawl_queue:
        url=crawl_queue.pop()
        html=download3(url).decode('utf-8')
        # filter for links matching our regular expression
        for link in get_links(html):
            if re.match(link_regex, link):
                # add this link to the crawl queue
                crawl_queue.append(link)
                
def link_crawler2(seed_url, link_regex):
    """Craw from the given seed URL following links matched by link_regex
    """
    crawl_queue=[seed_url] # the queue of URL's to download
    seen=set(crawl_queue)
    while crawl_queue:
        url=crawl_queue.pop()
        html=download3(url)
        sleep(1)
        if html is not None:
            html=html.decode('utf-8')
            print(len(get_links(html)))
            for link in get_links(html):
                # check if link matches expected regex
                if re.match(link_regex, link):
                    # form absolute link
                    link=urllib.parse.urljoin(seed_url, link)
                    # check if have already seen this link
                    if link not in seen:
                        crawl_queue.append(link)
#                 else:
#                     print('Not match:'+link)

def link_crawler(seed_url, link_regex=None, delay=5, max_depth=-1, max_urls=-1, headers=None, user_agent='wswp', proxy=None, num_retries=1):
    """Crawl from the given seed URL following links matched by link_regex
    """
    # the queue of URL's that still need to be crawled
    crawl_queue = deque([seed_url])
    # the URL's that have been seen and at what depth
    seen = {seed_url: 0}
    # track how many URL's have been downloaded
    num_urls = 0
    rp = get_robots(seed_url)
    throttle = Throttle(delay)
    headers = headers or {}
    if user_agent:
        headers['User-agent'] = user_agent

    while crawl_queue:
        url = crawl_queue.pop()
        # check url passes robots.txt restrictions
        if rp.can_fetch(user_agent, url):
            throttle.wait(url)
            html = download(url, headers, proxy=proxy, num_retries=num_retries)
            if html and html is not None:
                html=html.decode('utf-8')
                sleep(1)
                links = []
    
                depth = seen[url]
                if depth != max_depth:
                    # can still crawl further
                    if link_regex:
                        # filter for links matching our regular expression
                        links.extend(link for link in get_links(html) if re.match(link_regex, link))
    
                    for link in links:
                        link = normalize(seed_url, link)
                        # check whether already crawled this link
                        if link not in seen:
                            seen[link] = depth + 1
                            # check link is within same domain
                            if same_domain(seed_url, link):
                                # success! add this new link to queue
                                crawl_queue.append(link)
    
                # check whether have reached downloaded maximum
                num_urls += 1
                if num_urls == max_urls:
                    break
        else:
            print('Blocked by robots.txt:', url)

class Throttle:
    """Throttle downloading by sleeping between requests to same domain
    """
    def __init__(self, delay):
        # amount of delay between downloads for each domain
        self.delay=delay
        # timestamp of when a domain was last accessed
        self.domains={}
    
    def wait(self, url):
        domain=urllib.parse.urlparse(url).netloc
        last_accessed=self.domains.get(domain)
        
        if self.delay > 0 and last_accessed is not None:
            sleep_secs=self.delay-(datetime.now()-last_accessed).secondes
            if sleep_secs > 0:
                time.sleep(sleep_secs)
        self.domains[domain]=datetime.now()

def download(url, headers, proxy, num_retries, data=None):
    print('Downloading:', url)
    request=urllib.request.Request(url,data,headers)
    opener=urllib.request.build_opener()
    if proxy:
        proxy_params={urllib.parse.urlparse(url).scheme: proxy}
        opener.add_handler(urllib.request.ProxyHandler(proxy_params))
    try:
        response=opener.open(request)
        html=response.read();
        code=response.code
    except urllib.error.URLError as e:
        print('Downloading error:',e.reason)
        html=''
        if hasattr(e, 'code'):
            code=e.code
            if num_retries > 0 and 500 <= code <600:
                # retry 5XX HTTP errors
                return download(url, headers, proxy, num_retries-1, data)
        else:
            code=None
    return html

def normalize(seed_url, link):
    """Normalize this URL by removing hash and adding domain
    """
    link,_=urllib.parse.urldefrag(link) # remove hash to avoid duplicates
    return urllib.parse.urljoin(seed_url, link)

def same_domain(url1, url2):
    """Return True if both URL by removing hash and adding domain
    """
    url1=urllib.parse.urlparse(url1).netloc
    url2=urllib.parse.urlparse(url2).netloc
    return url1==url2
                    
def get_robots(url):
    """Initialize robots parser for this domain
    """
    rp=robotparser.RobotFileParser()
    rp.set_url(urllib.parse.urljoin(url, '/robots.txt'))
    rp.read()
    return rp
            
def get_links(html):
    """Return a list of links from html
    """
    # a regular expression to extract all links from the web page
    pattern='<a[^>]+href=["\'](.*?)["\']'
    webpage_regex=re.compile(pattern, re.RegexFlag.IGNORECASE)
    # list of all links from the web page
    return webpage_regex.findall(html)


#link_crawler2('http://example.webscraping.com', '(.*?)/(index|view)')
link_crawler('http://example.webscraping.com', '(.*?)/(index|view)', delay=0, num_retries=1, user_agent='BadCrawler')
#link_crawler('http://example.webscraping.com', '(.*?)/(index|view)', delay=0, num_retries=1, max_depth=1, user_agent='GoodCrawler')