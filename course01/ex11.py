#!/usr/bin/python3
'''
Created on Nov 30, 2018

@author: wizard
'''

def main():
    conn = dict(host='localhost', port=3306,service='mysql')
    
    for key in conn:
        print('key={} value={}'.format(key,conn[key]))

    for idx,key in enumerate(conn):
        print('index = {} key = {}'.format(idx,key))
    #N 1    
    for key,value in conn.items():
        #print('key {} value {}'.format(key,value))
        print('key ' + key + ' value ' + str(value))
        
if __name__ == '__main__':
    main()