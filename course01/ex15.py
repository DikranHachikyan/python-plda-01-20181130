#!/usr/bin/python3
'''
Created on Nov 30, 2018

@author: wizard
'''

def main():
    lst = [ x<<1 for x in range(10)]
    print('list:',lst)
        
if __name__ == '__main__':
    main()