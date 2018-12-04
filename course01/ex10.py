#!/usr/bin/python3
'''
Created on Nov 30, 2018

@author: wizard
'''

def main():
    tpl = ['python','c++','java','c']
    
    for value in tpl:
        print('value={}'.format(value))

    for idx,value in enumerate(tpl,1):
        print('index = {} value = {}'.format(idx,value))
        
if __name__ == '__main__':
    main()