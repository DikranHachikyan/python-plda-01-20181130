#!/usr/bin/python3
'''
Created on Nov 30, 2018

@author: wizard
'''

def sqGen(n):
    while n > 0:
        yield n * n
        n -= 1

def main():
    for x in sqGen(10):
        print('x=',x)
        
if __name__ == '__main__':
    main()