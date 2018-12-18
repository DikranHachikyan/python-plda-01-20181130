'''
Created on Jul 15, 2016

@author: wizard
'''
import re
   
if __name__ == '__main__':
    text = r"Your download should start shortly. If it doesn't, please use the direct link."
    
    result = re.findall(r'\w{2}',text)
    print('1:',result)
    
    # \b - word boundary
    result = re.findall(r'\b\w{2}',text)
    print('2:',result)
    
    # \b - word boundary
    result = re.findall(r'\w{2}\b',text)
    print('3:',result)
    
    # \b - word boundary
    result = re.findall(r'\B\w{2}',text)
    print('4:',result)
    
    # \b - word boundary
    result = re.findall(r'\B\w{2}\B',text)
    print('5:',result)
    
    print( re.sub(r'\Ba\B',r'#','alabama'))
    
    #
    result = re.findall(r'(\w{2})t',r'Your download should start shortly')
    print('6:',result)