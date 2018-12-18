'''
Created on Jul 15, 2016

@author: wizard
'''
import os
   
if __name__ == '__main__':
    fileName = 'lorem.txt'
    path = os.path.abspath(fileName)
    
    print('base name:', os.path.basename(path))
    print('dir name:', os.path.dirname(path))
    print('ext:', os.path.splitext(path))
    print('split:', os.path.split(path))
    
    readme_path = os.path.join(os.path.dirname(path), '..','..','docs','readme.txt')
    print(readme_path)
    print(os.path.normpath(readme_path))
