    
#!/usr/bin/python3
'''
Created on Nov 30, 2018

@author: wizard
'''
def cFilter(func,*array):
    res = []
    for v in array:
        if func(v):
            res.append(v)
    return res

def crit(v):
    return v % 2 != 0

def main():
    fn = lambda x: x**2 if x % 2 == 0 else x
    
    print('result:', fn(6))
    print('result:', fn(5))
    
    items = [('A',5,7), ('D',2,6), ('B',4,6)]
    items.sort()
    print('items:',items)
    items.sort(key=lambda el:(el[1]))
    print('items:',items)
    items.sort(key=lambda el:(el[2],el[0]))
    print('items:',items)
    
    lst = [ x**2 for x in range(1,6)]
    print('list:', lst)
    lstf = cFilter(lambda x: x % 2 == 0, *lst )
    print('list:', lstf)
    
    lstf = cFilter(crit, *lst )
    print('list:', lstf)
    
        
if __name__ == '__main__':
    main()