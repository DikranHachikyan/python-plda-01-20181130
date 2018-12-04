#!/usr/bin/python3
'''
Created on Nov 30, 2018

@author: wizard
'''

def main():
    i = 0
    
    while i < 10:
        i += 1
        if i % 2 != 0: continue
        print('i=', i)
    else:
        print('else...')
        
if __name__ == '__main__':
    main()