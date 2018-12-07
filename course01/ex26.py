#!/usr/bin/python3
'''
Created on Nov 30, 2018

@author: wizard
'''
from functools import wraps

def pow2(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        lst = [ val**2 for val in func(*args,**kwargs)]
        return lst
    return wrapper

@pow2
def genNums(n):
    while n > 0:
        yield n
        n -= 1

def main():
    for i in genNums(6):
        print(i)
    
        
if __name__ == '__main__':
    main()
