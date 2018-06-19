'''
Created on Jun 19, 2018

@author: xiongan2
'''
import json

if __name__ == '__main__':
    print(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]))
    print(json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]'))