'''
Created on Jul 15, 2016

@author: wizard
'''
import os
   
if __name__ == '__main__':
    fileName = 'lorem.txt'
    path = os.path.dirname( os.path.abspath(fileName))
    
    print('path:',path)
    print('abs path:', os.path.abspath(fileName))
    
    print('is file:',fileName, ' ', os.path.isfile(fileName))
    print('is dir:',path, ' ', os.path.isdir(path))
    