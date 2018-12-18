'''
Created on Jul 15, 2016

@author: wizard
'''

   
if __name__ == '__main__':
    with open('output.bin','wb') as fwb:
        fwb.write(b'Consectetur adipisicing elit, sed do eiusmod')
        
    with open('output.bin','rb') as frb:
        print( frb.read())