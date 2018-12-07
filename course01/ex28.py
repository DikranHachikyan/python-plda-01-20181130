#!/usr/bin/python3
'''
Created on Nov 30, 2018

@author: wizard
'''


def main():
    b = 4
    
    try:
        a = int(input('value:'))
        print('{} + {} = {}'.format(a, b, a + b))
    except TypeError as e:
        print('Exception 1:',e)
    except  ValueError as e:
        print('Exception 2:', e)
    except:
        print('Unknown Error!')
    else:
        print('else...')
    finally:
        print('finally...')       
    
        
if __name__ == '__main__':
    main()
