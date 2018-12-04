#!/usr/bin/python3
'''
Created on Nov 30, 2018

@author: wizard
'''

def suma(a,b, *args):
    c = a +b
    for v in args:
        c += v
        
    return c

def main():
    x,y = 5,6
    res = suma(x,y)
    print('{} + {} = {}'.format(x,y,res))
    
    z = 8
    res = suma(x,y,z);
    print('{} + {} + {} = {}'.format(x,y,z,res))
    
    res = suma(x,y,1,2,3,4)
    print('1+2+...+ 5 = {}'.format(res))
    
    lst = [v for v in range(1,5)]
    res = suma(x,y, *lst)
    print(' + '.join( map(str,lst) )+' + {} + {} = {}'.format(x,y,res))
    print(' + '.join( str(v) for v in lst )+' + {} + {} = {}'.format(x,y,res))
        
if __name__ == '__main__':
    main()