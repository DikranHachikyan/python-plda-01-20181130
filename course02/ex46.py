'''
Created on Jul 15, 2016

@author: wizard
'''
import re
   
if __name__ == '__main__':
    text = r'wizard:x:1000:1000:Dikran Hachikyan,Sofia,02/123-34-56,d@no.com:/home/wizard:/bin/bash'

    result = re.split(r'[:,]',text)
    print(result)