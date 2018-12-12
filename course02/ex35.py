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
        
    @property
    def x(self):
        #print('get x method')
        return self._x
    
    @x.setter
    def x(self, v):
        #print('set x method')
        self._x = v

#===============================================================================
#   Class Shape
#===============================================================================

class Shape:
    def area(self):
        return self._width * self._height
              
#===============================================================================
#   Class Rectangle
#===============================================================================

class Rectangle(Point,Shape):
    
    def __init__(self, width=0, height=0, *args, **kwargs):
        super().__init__(*args, **kwargs) # изпълнява констр. на родителя
        self._width = width
        self._height = height
        
    def draw(self):
        super().draw()
        print('Rectangle width={} height={}'.format( self._width, self._height))
        
    
if __name__ == '__main__':
    #===========================================================================
    # r = Rectangle(100,200)
    # 
    # r.draw()
    #===========================================================================
    data = {
         'x':15,
         'y':25,
         'width':120,
         'height':240
         }
    
    r = Rectangle( **data ) # Rectangle( x = 15, y = 25 , ... )
    
    r.draw()
    print('Area:',r.area())
    