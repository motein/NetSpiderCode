'''
Created on Jun 14, 2018

@author: xiongan2
'''
from pymongo import MongoClient

client=MongoClient('localhost', 27017)
print(client.address)
db=client.cache
url='https://www.baidu.com'
html='...'
new_html='New HTML'
db.webpage.insert({'url': url, 'html': html})
print(db.webpage.find_one({'url':url}))
id=db.webpage.find_one({'url':url})['_id']
print(db.webpage.find())
db.webpage.update({'_id': id}, {'$set': {'html': new_html}}, upsert=True)
print(db.webpage.find_one({'url':url}))
print(db.webpage.find().count())
client.close()