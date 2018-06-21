'''
Created on Jun 21, 2018

@author: xiongan2
'''
from urllib import request, parse
import lxml.html
from http import cookiejar
from io import BytesIO
import base64
from PIL import Image
import pprint


REGISTER_URL = 'http://example.webscraping.com/places/default/user/register'


def extract_image(html):
    tree = lxml.html.fromstring(html)
    img_data = tree.cssselect('div#recaptcha img')[0].get('src')
    # remove data:image/png;base64, header
    img_data = img_data.partition(',')[-1]
    print(type(img_data))
    #open('test_.png', 'wb').write(data.decode('base64'))
    binary_img_data = base64.b64decode(img_data)
    file_like = BytesIO(binary_img_data)
    img = Image.open(file_like)
    #img.save('test.png')
    return img



def parse_form(html):
    """extract all input properties from the form
    """
    tree = lxml.html.fromstring(html)
    data = {}
    for e in tree.cssselect('form input'):
        if e.get('name'):
            data[e.get('name')] = e.get('value')
    return data



def register(first_name, last_name, email, password, captcha_fn):
    cj = cookiejar.CookieJar()
    opener = request.build_opener(request.HTTPCookieProcessor(cj))
    html = opener.open(REGISTER_URL).read()
    form = parse_form(html)
    form['first_name'] = first_name
    form['last_name'] = last_name
    form['email'] = email
    form['password'] = form['password_two'] = password
    img = extract_image(html)
    if img is not None:
        print(' extract image successfully')
    if captcha_fn is None:
        print('Callback function not set')
        return False
    captcha = captcha_fn(img)
    print("content:", captcha)
    form['recaptcha_response_field'] = captcha
    encoded_data = bytes(parse.urlencode(form), 'utf-8')
    print(type(encoded_data))
    #encoded_data = bytes(parse.urlencode(encoded_data), 'utf-8')
    req = request.Request(REGISTER_URL, encoded_data)
    print(type(encoded_data))
    res = opener.open(req)
    print(res.geturl())
    success = '/user/register' not in res.geturl()
    return success

def test_basic():
    cj = cookiejar.CookieJar()
    opener = request.build_opener(request.HTTPCookieProcessor(cj))
    html = opener.open(REGISTER_URL).read()
    form = parse_form(html)
    pprint.pprint(form)

if __name__ == '__main__':
    #test_basic()
    register('aaa', 'bbb', 'motein@126.com', 'ccccccccccdfa', None)
    