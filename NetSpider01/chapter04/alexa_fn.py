'''
Created on Jun 14, 2018

@author: Xor
'''
import csv
from zipfile import ZipFile
from io import BytesIO, TextIOWrapper
from chapter03.downloader import Downloader

def alexa():
    D=Downloader()
    zipped_data=D('http://s3.amazonaws.com/alexa-static/top-1m.csv.zip')
    print(type(zipped_data))
    urls=[] # top 1 million URL's will be stored in this list
    with ZipFile(BytesIO(zipped_data)) as zf:
        csv_filename = zf.namelist()[0]
        print(csv_filename)
        mess=zf.open(csv_filename)
        for website in mess.readlines():
            webstr=website.decode('utf-8').replace("\n","").split(',')[1]
            print(webstr)
            urls.append('http://' + webstr)
    return urls

def alexa1(): # Read local file
    urls=[] # top 1 million URL's will be stored in this list
    with ZipFile('E:/top-1m.csv.zip') as zf:
        csv_filename = zf.namelist()[0]
        print(csv_filename)
        mess=zf.open(csv_filename)
        for website in mess.readlines():
            webstr=website.decode('utf-8').replace("\n","").split(',')[1]
            print(webstr)
            urls.append('http://' + webstr)
    return urls

def alexa2():
    D=Downloader()
    zipped_data=D('http://s3.amazonaws.com/alexa-static/top-1m.csv.zip')
    print(type(zipped_data))
    urls=[] # top 1 million URL's will be stored in this list
    with ZipFile(BytesIO(zipped_data)) as zf:
        csv_filename = zf.namelist()[0]
        print(csv_filename)
        mess=zf.open(csv_filename, 'r')
        mess=TextIOWrapper(mess)
        print(mess)
        for _, website in csv.reader(mess):
            print(_, website)
            urls.append('http://' + website)
    return urls

if __name__ == '__main__':
    print(len(alexa2()))