#!/usr/bin/python3
'''
Created on Nov 30, 2018

@author: wizard
'''

if __name__ == '__main__':
    ''' Tuple '''
    tpl = (10,12,34,56)
    print('tpl[1]=',tpl[1])
    #tpl[1] = 100 # Error immutable
    print('tpl->',tpl)
    
    ''' List '''
    lst = [10,20,30,49,66]
    print('lst[3]=', lst[3])
    print('lst->', lst)
    lst.append(100)
    print('lst->', lst)
    lst[:] = range(10)
    print('lst->', lst)
                  
    lst[:] = range( 3, 10, 2) #start,stop,step
    print('lst->', lst)
    
    lst[:] =  range(10)
    print('lst[1:5:2]=', lst[1:5:2])
    
    ''' Dictionary '''
    conn = dict(host = 'localhost', port = dict(n=3306,name='mysql'), db = 'sales', connected = True)
    
    print('Connected to {} on port {} database {}'.format(conn['host'],
                                                          conn['port'],
                                                          conn['db']))
    
    #Python 3^ (JSON - JavaScript Object Notation)
    
    app = {
          'title':'My App'
        , 'version': '2.3.5'
        , 'path': '/app/'
    }
    
    app['version'] = '2.5.5'
    print('app data:', app)
        