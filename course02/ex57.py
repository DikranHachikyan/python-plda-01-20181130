#!/usr/bin/python3
'''
Created on Jul 15, 2016

@author: wizard
'''
import os

   
if __name__ == '__main__':
    for root, dirs, files in os.walk('../../hw'):
        print(os.path.abspath(root))
        if dirs:
            print('Directories:')
            for dirName in dirs:
                print(dirName)
        if files:
            print('Files:')
            for fileName in files:
                print(fileName)
