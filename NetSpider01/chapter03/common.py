'''
Created on Jun 13, 2018

@author: Xor
'''
import time

def time_elapse(fn):
    def _wrapper(*args, **kwargs):
        start = time.clock()
        fn(*args, **kwargs)
        print("%s cost %s second"%(fn.__name__, time.clock() - start))
    return _wrapper

# @time_elapse
# def test(x):
#     time.sleep(x)
# 
# test(4)