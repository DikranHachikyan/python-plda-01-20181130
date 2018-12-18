#!/usr/bin/python3
'''
Created on Jul 15, 2016

@author: wizard
'''
import os
import shutil
   
if __name__ == '__main__':
    base_path = 'examples'
    
    os.mkdir(base_path)
    #os.makedirs(base_path, exist_ok=True)
    
    path_b = os.path.join(base_path, 'a','b')
    path_c = os.path.join(base_path, 'a','c')
    path_d = os.path.join(base_path, 'a','d')
    
    os.makedirs(path_b)
    os.makedirs(path_c)
    
    for fileName in ('ex1.txt','ex2.txt','ex3.txt'):
        with open( os.path.join(path_b, fileName),'w') as fw:
            fw.write( f'Lorem ipsum dolor sit amet: {fileName}' )  
            
    shutil.move(path_b, path_d)
    shutil.move(
         os.path.join(path_d, 'ex1.txt')
        ,os.path.join(path_d, 'ex1c.txt')
    )  
    