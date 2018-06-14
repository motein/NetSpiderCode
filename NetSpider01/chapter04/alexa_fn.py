'''
Created on Jun 14, 2018

@author: Xor
'''
import csv
from zipfile import ZipFile
from io import StringIO
from chapter03.downloader import Downloader

def alexa():
#     D=Downloader()
#     zipped_data=D('http://s3.amazonaws.com/alexa-static/top-1m.csv.zip')
    urls=[] # top 1 million URL's will be stored in this list
#     with ZipFile(StringIO(zipped_data)) as zf:
    with ZipFile('E:/top-1m.csv.zip') as zf:
        csv_filename = zf.namelist()[0]
        print(csv_filename)
        mess=zf.open(csv_filename)
        #for _, website in csv.reader(mess):
        for website in mess.readlines():
            webstr=website.decode('utf-8').replace("\n","").split(',')[1]
            print(webstr)
            urls.append('http://' + webstr)
    return urls

print(len(alexa()))