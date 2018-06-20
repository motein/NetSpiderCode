'''
Created on Jun 20, 2018

@author: xiongan2
'''
from urllib import request, parse
import lxml.html
import pprint
import os
import json
import glob
import sqlite3
import time
from http import cookiejar

LOGIN_URL = 'http://example.webscraping.com/places/default/user/login'
LOGIN_EMAIL = 'example@webscraping.com'
LOGIN_PASSWORD = 'example'
COUNTRY_URL = 'http://example.webscraping.com/edit/United-Kingdom-239'

def login_basic():
    """fails because not using formkey
    """
    data = {'email':LOGIN_EMAIL, 'password':LOGIN_PASSWORD}
    encoded_data = bytes(parse.urlencode(data), 'utf-8')
    print(type(encoded_data))
    req = request.Request(LOGIN_URL, encoded_data)
    res = request.urlopen(req)
    print(res.geturl()) # Still login URL
    

    
def login_formkey():
    """fails because not using cookies to match formkey
    """
    html = request.urlopen(LOGIN_URL).read()
    data = parse_form(html)
    data['email'] = LOGIN_EMAIL
    data['password'] = LOGIN_PASSWORD
    encoded_data = bytes(parse.urlencode(data), 'utf-8')
    req = request.Request(LOGIN_URL, encoded_data)
    res = request.urlopen(req)
    print(res.geturl())

def login_cookies():
    """working login
    """
    cj = cookiejar.CookieJar()
    opener = request.build_opener(request.HTTPCookieProcessor(cj))
    html = opener.open(LOGIN_URL).read()
    data = parse_form(html)
    data['email'] = LOGIN_EMAIL
    data['password'] = LOGIN_PASSWORD
    encoded_data = bytes(parse.urlencode(data), 'utf-8')
    req = request.Request(LOGIN_URL, encoded_data)
    res = opener.open(req)
    print(res.geturl())
    return opener

def login_firefox():
    """load cookies from firefox
    """
    session_filename = find_ff_sessions()
    cj = load_ff_sessions(session_filename)
    opener = request.build_opener(request.HTTPCookieProcessor(cj))
    html = opener.open(COUNTRY_URL).read()

    tree = lxml.html.fromstring(html)
    print(tree.cssselect('ul#navbar li a')[0].text_content())
    return opener

def parse_form(html):
    tree = lxml.html.fromstring(html)
    data ={}
    for e in tree.cssselect('form input'):
        if e.get('name'):
            data[e.get('name')]=e.get('value')
    return data

def check_name():
    html = request.urlopen(LOGIN_URL).read()
    form = parse_form(html)
    pprint.pprint(form)
    
def load_ff_sessions(session_filename):
    cj = cookiejar.CookieJar()
    if os.path.exists(session_filename):  
        try: 
            json_data = json.loads(open(session_filename, 'rb').read())
        except ValueError as e:
            print('Error parsing session JSON:', str(e))
        else:
            for window in json_data.get('windows', []):
                for cookie in window.get('cookies', []):
                    pprint.pprint(cookie)
                    c = cookiejar.Cookie(0, cookie.get('name', ''), cookie.get('value', ''), 
                        None, False, 
                        cookie.get('host', ''), cookie.get('host', '').startswith('.'), cookie.get('host', '').startswith('.'), 
                        cookie.get('path', ''), False,
                        False, str(int(time.time()) + 3600 * 24 * 7), False, 
                        None, None, {})
                    cj.set_cookie(c)
    else:
        print('Session filename does not exist:', session_filename)
    return cj


def find_ff_sessions():
    paths = [
        '~/.mozilla/firefox/*.default',
        '~/Library/Application Support/Firefox/Profiles/*.default',
        '%APPDATA%/Roaming/Mozilla/Firefox/Profiles/*.default'
    ]
    for path in paths:
        filename = os.path.join(path, 'sessionstore.js')
        matches = glob.glob(os.path.expanduser(filename))
        if matches:
            return matches[0]

    
if __name__ == '__main__':
    #login_basic()
    #check_name()
    #login_formkey()
    login_cookies()

