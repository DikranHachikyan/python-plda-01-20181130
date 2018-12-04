#!/usr/bin/python3
'''
Created on Nov 30, 2018

@author: wizard
'''

def suma(a,b,d=0):
    c = a + b + d
    return c

def main():
    x,y = 5,6
    res = suma(x,y)
    print('{} + {} = {}'.format(x,y,res))
    
    z = 8
    res = suma(x,y,z);
    print('{} + {} + {} = {}'.format(x,y,z,res))
    
        
if __name__ == '__main__':
    main()