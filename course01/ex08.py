#!/usr/bin/python3
'''
Created on Nov 30, 2018

@author: wizard
'''

def main():
    i = 1
    suma = 0
    
    while i <= 100:
        suma += i
        i += 1
    else:
        print('else ...')
        
    print('1+2+...+99+100 = {}'.format(suma))
            
if __name__ == '__main__':
    main()