#!/usr/bin/python3
'''
Created on Nov 30, 2018

@author: wizard
'''

class Point:
    def __init__(self, x = 0, y = 0, *args, **kwargs):
        ''' Constructor '''
        self.x = x
        self.y = y

    def moveTo(self, dx,dy):
        self.x += dx
        self.y += dy
        
    def draw(self):
        print('({},{})'.format(self.x,self.y))
        
if __name__ == '__main__':
    p1 = Point(10,-20)
    p2 = Point(2,6)
    
    #print('Point 1 ({},{})'.format(p1.x, p1.y))
    #print('Point 2 ({},{})'.format(p2.x, p2.y))
    
    p1.moveTo(120, 130)
    
    p1.draw()
