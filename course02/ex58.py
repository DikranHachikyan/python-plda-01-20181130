
#!/usr/bin/python3
'''
Created on Jul 15, 2016

@author: wizard
'''
import os
from fnmatch import filter
import gzip
import re

def gFindFiles(fpattern, top):
    for path, dirs, files in os.walk(top):
        for name in filter(files, fpattern):
            yield os.path.join(path, name)

def gOpenFiles(fileNames):
    for fileName in fileNames:
        try:
            if fileName.endswith('.gz'):
                fr = gzip.open(fileName,'rt')    
            else:
                fr = open(fileName,'rt')
        except:
            pass
        yield fr
        #fr.close() 

def gReadLines(fileHandle):
    for line in fileHandle:
        yield from line

def gGrepLines(pattern, lines):
    p = re.compile(pattern)
    for line in lines:
        if p.search(line):
            yield line
          
if __name__ == '__main__':
    syslogs = gFindFiles('syslog*', '/var/log/')
    files   = gOpenFiles(syslogs)
    lines   = gReadLines(files)
    found   = gGrepLines('NetworkManager', lines)
    
    for x in found:
        print(x)