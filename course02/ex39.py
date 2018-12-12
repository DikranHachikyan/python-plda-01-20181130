'''


@author: wizard
'''
import re
    
if __name__ == '__main__':
    txt = "hello python and java, javascript"
    pattern = re.compile( r"(\w+)")
    for m in pattern.finditer(txt):
        print('Start:', m.start(), ' End:', m.end(), ' Span:',m.span(), ' Group:', m.group(1))