#!/usr/bin/python3
'''
Created on Nov 30, 2018

@author: wizard
'''


if __name__ == '__main__':
    x = int(input('x='))
    #print('type of ', type(x) ,x)
    if x > 10 :
        print('{} > 10'.format(x))
    else:
        print('{} <= 10'.format(x))
        
        
    m = 20 if x > 3 else 15
    #m = (x > 4)? 10:20
    print('x {} m {}'.format(x,m))
    #print('val = ', ((x > 4)? 10 : -10))
    