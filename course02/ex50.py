'''
Created on Jul 15, 2016

@author: wizard
'''

   
if __name__ == '__main__':
    
    try:
        #Context Manager __enter__, __exit__
        with open('lorem.txt') as fh: 
            for line in fh:
                #print(line, end='')
                print(line.strip())
                
    except FileNotFoundError as e:
        print(e)
    