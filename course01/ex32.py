#!/usr/bin/python3
'''
Created on Nov 30, 2018

@author: wizard
'''

class Point:
    count = 0 #Обща за всички обекти (променлива на класа не на обекта)
    def __init__(self, x = 0, y = 0, *args, **kwargs):
        ''' Constructor '''
        self.x = x
        self.y = y
        self._visible = True if self.x >0 and self.y >0 else False
        Point.count +=1 

    def moveTo(self, dx,dy):
        #TODO: update visible
        self.x += dx
        self.y += dy
        
    def draw(self):
        print('({},{}) #{}'.format(self.x,self.y, Point.count))
        
if __name__ == '__main__':
    p1 = Point(10,-20)
    p2 = Point(2,6)
    #__len()__ private method
    print('xxxx'.__len__())
    #print('Point 1 ({},{})'.format(p1.x, p1.y))
    #print('Point 2 ({},{})'.format(p2.x, p2.y))
    
    p1.moveTo(120, 130)
    
    p1.draw()
    #Грешка count се създава на ново и се закача за обекта <> Point.count
    #p2.count = 100
    #print('Point 2 ({},{}) #{}'.format(p2.x, p2.y,p2.count))
    p2.draw()