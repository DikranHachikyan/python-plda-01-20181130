'''
Created on Jul 15, 2016

@author: wizard
'''

   
if __name__ == '__main__':
    fh = open('lorem.txt','rt')  #read,text
    
    for line in fh:
        #print(line, end='')
        print(line.strip())
        
    fh.close()