'''
Created on Jul 15, 2016

@author: wizard
'''
import re
   
if __name__ == '__main__':
    text = r'''
        Maria Anders
        John Doe
        Anna Smith
        Peter Weiss
    '''
    # M.Anders
    result = re.sub(r'\s', r'-', re.sub(r'\n', r'#',text))
    print('0:',result)
     
    result = re.findall(r'(\w)\w+\s(\w+)',text)
    print(result)
    
    result = re.sub(r'\s*(\w)\w+\s(\w+)\s*\n', r'\1.\2,', text)
    print('2:',result)
    #re.split(r'\n',
    result =  re.split(r',', re.sub(r',\s*$', r'',result) )
    print('3:',result)
    