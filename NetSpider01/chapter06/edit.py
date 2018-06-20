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
import mechanicalsoup
from chapter06.login import login_cookies, parse_form

from http import cookiejar
import chapter06

COUNTRY_URL = 'http://example.webscraping.com/edit/United-Kingdom-239'

def edit_country():
    opener = login_cookies()
    country_html = opener.open(COUNTRY_URL).read()
    data = parse_form(country_html)
    pprint.pprint(data)
    print('Population before: ' + data['population'])
    data['population'] = int(data['population']) + 1
    encoded_data = parse.urlencode(data)
    req = request.Request(COUNTRY_URL, encoded_data)
    res = opener.open(req)

    country_html = opener.open(COUNTRY_URL).read()
    data = parse_form(country_html)
    print('Population after:', data['population'])



def mechanize_edit():
    """Use mechanize to increment population
    """
    # login
    br = mechanicalsoup.Browser()
    br.open(chapter06.login.LOGIN_URL)
    br.select_form(nr=0)
    print(br.form)
    br['email'] = chapter06.login.LOGIN_EMAIL
    br['password'] = chapter06.login.LOGIN_PASSWORD
    res = br.submit()

    # edit country
    br.open(COUNTRY_URL)
    br.select_form(nr=0)
    print('Population before:', br['population'])
    br['population'] = str(int(br['population']) + 1)
    br.submit()

    # check population increased
    br.open(COUNTRY_URL)
    br.select_form(nr=0)
    print('Population after:', br['population'])

if __name__ == '__main__':
    edit_country()
    mechanize_edit()