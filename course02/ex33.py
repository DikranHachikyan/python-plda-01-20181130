'''

@author: wizard
'''
class Point:
    count = 0 # Обща за всички обекти
    def __init__(self, x=0, y=0, *args, **kwargs):
        self._x = x
        self.y = y
        #self.__visible = True
        self._visible = True # Прието е така
        Point.count +=1
    
    def __del__(self):
        print('Destructor Point')
        Point.count -=1
        
    def moveTo(self,x,y):
        self._x = x
        self.y = y
        
    def draw(self):
        print('Point x={} y={} number of objects:{}'.format( self._x , self.y, Point.count ))
        
    def _get_x(self):
        print('get x method')
        return self._x
    
    def _set_x(self,x):
        print('set x method')
        self._x = x
        
    x = property(_get_x, _set_x, doc='x position') 
 
        
if __name__ == '__main__':
    p = Point(10,20)
    
    p.x = 15
    
    print(p.x)
    
    