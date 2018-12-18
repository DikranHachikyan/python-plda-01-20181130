#!/usr/bin/python3
'''
Created on Jul 15, 2016

@author: wizard
'''
import os
from tempfile import NamedTemporaryFile, TemporaryDirectory
   
if __name__ == '__main__':
    with TemporaryDirectory(dir='.') as tempDir:
        print('temporary directory:' , tempDir)
        with NamedTemporaryFile(dir=tempDir) as tmp:
            name = tmp.name
            print( os.path.abspath(name))
            input()