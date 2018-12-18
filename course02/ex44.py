'''
Created on Jul 15, 2016

@author: wizard
'''
import re
   
if __name__ == '__main__':
    text = r"anna@gmail.com, john@vision.onmicro.soft.com, maria@sales.biz, dev@angular.io"
    
    result = re.findall(r'@(\w+(?:\.\w+)*)',text)
    print('1:',result)
    
    result = re.findall(r'@\w+(\.\w+)*',text)
    print('2:',result)
