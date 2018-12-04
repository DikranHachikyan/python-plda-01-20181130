#!/usr/bin/python3
'''
Created on Nov 30, 2018

@author: wizard
'''

def main():
    i = 0
    
    while i < 10:
        print('i=', i)
        i += 1
        if i == 4: break
    else:
        print('else...')
        
if __name__ == '__main__':
    main()