#!/usr/bin/python3
'''
Created on Nov 30, 2018

@author: wizard
'''

def genText( *args):
    for v in args:
        yield v

def main():
    lst = ['python','java','c++','c']
    
    for txt in genText(*lst):
        print(txt)
    
    gn = genText(*lst)
    
    print('next value:', next(gn))
    print('next value:', next(gn))
    print('next value:', next(gn))
    
        
if __name__ == '__main__':
    main()