'''

@author: wizard
'''
import re
    
if __name__ == '__main__':
    names = None
    pattern = re.compile( r"\s*(?P<first>[A-Z][a-z]+)\s+(?P<last>[A-Z][a-z]+)")
    while names == None:
        names = input("Your names (Firstname Lastname):")
        m = pattern.match(names)
        if m:
            print(names, 'Group:', m.group(), ' F N:', m.group('first') , ' L N:', m.group('last') )
        else:
            names = None