#!/usr/bin/python3
'''
Created on Nov 30, 2018

@author: wizard
'''

def suma(a,b):
    c = a + b
    return c

def main():
    x,y = 5,6
    res = suma(x,y)
    print('{} + {} = {}'.format(x,y,res))
        
if __name__ == '__main__':
    main()