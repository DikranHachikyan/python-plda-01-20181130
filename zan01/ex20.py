#!/usr/bin/python3
'''
Created on Nov 30, 2018

@author: wizard
'''

def show(title, *args, **kwargs):
    print('title = ', title)
    
    for v in args:
        print('v=',v)
        
    if 'author' in kwargs:
        print('Author:', kwargs['author'])
        
    if 'version' in kwargs:
        print('Veriosn', kwargs['version'])

def main():
    show('Text Editor')
    
    show('Text Editor', 1,2,3,4,'hello')
    
    app = {
       'name':'Text Editor'
     , 'version': '2.4.5'
     , 'author' : 'Anna Smith'
     , 'path'   : '/usr/local/'
    }
    lst = [v for v in range(1,5)]
    
    print('--------------------')    
    #ако ключа name се смени с title
    #show(**app)    
    show( app['name'], *lst, **app)    
if __name__ == '__main__':
    main()