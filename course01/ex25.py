#!/usr/bin/python3
'''
Created on Nov 30, 2018

@author: wizard
'''
from functools import wraps

def capitalText(func):
    """CapitalText"""
    @wraps(func)
    def wrapper(sep,*args):
        args = [val.upper() for val in args]
        return func(sep,*args)
    return wrapper


def brackets(func):
    """Brackets"""
    @wraps(func)
    def wrapper(sep,*args):
        args = [ '[{}]'.format(val) for val in args]
        return func(sep,*args)
    return wrapper

@brackets
@capitalText
def concat(sep,*args):
    """Concat"""
    return sep.join(args)

def main():
    names = ['python','java','c++','c']
    
    print('names:', concat('|', *names))
    print('name:', concat.__name__)
    print('doc:', concat.__doc__)
    
        
if __name__ == '__main__':
    main()
