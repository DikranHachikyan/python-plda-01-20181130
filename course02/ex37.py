'''

@author: wizard
'''
import re
    
if __name__ == '__main__':
    names = None
    pattern = re.compile( r"\s*([A-Z][a-z]+)\s+([A-Z][a-z]+)")
    while names == None:
        names = input("Your names (Firstname Lastname):")
        m = pattern.match(names)
        if m:
            print(names, 'Group:', m.group(), ' F N:', m.group(1) , ' L N:', m.group(2) )
        else:
            names = None