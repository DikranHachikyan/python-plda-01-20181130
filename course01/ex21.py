#!/usr/bin/python3
'''
Created on Nov 30, 2018

@author: wizard
'''

def show(title, path='/no/path/', *args, **kwargs):
    print('title = ', title)
    print('path=',path)
    for v in args:
        print('v=',v)
        
    if 'author' in kwargs:
        print('Author:', kwargs['author'])
        
    if 'version' in kwargs:
        print('Veriosn', kwargs['version'])

def main():
    app = {
       'name':'Text Editor'
     , 'version': '2.4.5'
     , 'author' : 'Anna Smith'
     , 'path'   : '/usr/local/'
    }
      
    show( app['name'],  **app)  
    show( name='Text Editor',title='Title',version='2.4.5',author='Maria Anders')  
      
if __name__ == '__main__':
    main()