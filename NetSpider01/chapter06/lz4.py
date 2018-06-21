'''
Created on Jun 21, 2018

@author: xiongan2
'''
from sys import stdout
import os
from chapter06.login import find_ff_sessions
import lz4

# def lz4_func(fstream, mode='-d'):
#     assert fstream.read(8) == b'mozLz40\0'
#     stdout.write(frame.decompress(fstream.read()))
#     
# def test():
#     session_filename = find_ff_sessions()
#     print(session_filename)
#     fstream = open(session_filename, 'rb')
#     lz4_func(fstream)
#     
# def test2():
#     input_data = 20 * 128 * os.urandom(1024)  # Read 20 * 128kb
#     compressed = frame.compress(input_data)
#     decompressed = frame.decompress(compressed)
#     print(decompressed == input_data)
        
if __name__ == '__main__':
    #test2()
    stdout.write('dfdsfsadfsad')