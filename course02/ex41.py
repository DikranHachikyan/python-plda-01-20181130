'''
Created on Jul 15, 2016

@author: wizard
'''
import re
   
if __name__ == '__main__':
    match = re.search(r'\d{3}\D\d{2}\D\d{2}', r'Phone: 123-45-67')
    print(match.group() if match else 'not found')
    
    match = re.fullmatch(r'[a-z]\d{2}\D\d{2}',r'A12-67', re.I)
    print(match.group() if match else 'not found' )
    
    text = r'Let:companies:apply to you. Get 5+ offers, in, one, week. Salaries: €35k-€100k'
    result = re.split(r'[:,]',text)
    print(result)
    
    result = re.findall(r'\d{2}\.\d{2}\.\d{4}',r'We could go there on 19.01.2018 or 01.09.2018')
    print(result)
    
    text = r'We could go there on 19.01.2018 or 01.09.2018'
    for m in re.finditer(r'\d{2}\.\d{2}\.\d{4}', text):
        print(m.group(), ' ', m.span())
        
    result = re.sub(r'\d{2}\.\d{2}\.\d{4}',r'dd.mm.yyyy',text)
    print(result)    
        