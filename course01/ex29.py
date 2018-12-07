#!/usr/bin/python3
'''
Created on Nov 30, 2018

@author: wizard
'''

def find( key, **lst):
    if key in lst:
        print(key,'->',lst[key])
    else:
        raise KeyError('Invalid Key:{}'.format(key))

def main():
    conn = {
        'host' : 'localhost'
      , 'port': 3306
    }      
    
    try:
        find('port', **conn);
        find('ip', **conn);
    except KeyError as e:
        print(e);
        
    find('gateway', **conn)
        
if __name__ == '__main__':
    main()
