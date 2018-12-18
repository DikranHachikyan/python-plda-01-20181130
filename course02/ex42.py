'''
Created on Jul 15, 2016

@author: wizard
'''
import re
   
if __name__ == '__main__':
    text = r"Your download should start shortly. If it doesn't, please use the direct link."
    
    result = re.findall(r'.',text)
    print('1:',result)
    
    result = re.findall(r'\w',text)
    print('2:',result)
    
    result = re.findall(r'\w+',text)
    print('3:',result)
    
    result = re.findall(r'^\w+|\w+$',text)
    print('4:',result)
    #За самостоятелна работа result = [Your, shortly, If, link ]
    result = re.findall(r'',text)
    print('5:',result)