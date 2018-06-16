'''
Created on Jun 16, 2018

@author: Xor
'''
from multiprocessing import Process

import os

def run_proc(name):
    print('hello', name)
    
def main():
    p = Process(target=run_proc, args=('bob',))
    p.start()
    p.join()

if __name__ == '__main__':
    main()