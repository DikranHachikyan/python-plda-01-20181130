#!/usr/bin/python3
'''
Created on Nov 30, 2018

@author: wizard
'''

class Point:
    pass

        
if __name__ == '__main__':
    p = Point()
    p1 = Point()
    
    p.x = 10
    p.y = 20
    
    print('Point ({},{})'.format(p.x,p.y))
    # AttributeError
    #print('Point ({},{})'.format(p1.x,p1.y))
    
