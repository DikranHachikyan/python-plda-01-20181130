#!/usr/bin/python3
'''
Created on Nov 30, 2018

@author: wizard
'''
def newFile():
    print('Create new file')
    
def openFile():
    print('Open file')
    
def saveFile():
    print('Save file')
    
def exitApp():
    print('Quit')
    
def main():
    action = {
        'n':newFile
      , 'o':openFile
      , 's':saveFile
      , 'e':exitApp
    }    
    
    ch = input('Enter n-new, o - open, s - save, e-exit:')
    
    if ch in action:
        action[ch]()
    else:
        print('Invalid input')
            
if __name__ == '__main__':
    main()