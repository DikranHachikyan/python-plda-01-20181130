#!/usr/bin/python3
'''
Created on Nov 30, 2018

@author: wizard
'''

if __name__ == '__main__':
    a = 10
    msg = 'Hello Python'
    
    print('a=',a);
    print('a = {} message: {}'.format(a, msg))
    
    print('Type of a is {} id {}'.format(type(a), id(a) ) )
    
    b = 10
    b += 2 # b = b + 2
    print('Type of b is {} id {}'.format(type(b), id(b) ) )
        