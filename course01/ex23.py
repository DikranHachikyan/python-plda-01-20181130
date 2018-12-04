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
    
#     print(genText(*lst))
#     print(genText(*lst))
#     print(genText(*lst))
        
if __name__ == '__main__':
    main()