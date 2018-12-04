#!/usr/bin/python3
'''
Created on Nov 30, 2018

@author: wizard
'''

if __name__ == '__main__':
    a = 10
    b = 3
    
    print('{} // {} = {}'.format(a,b,a//b))
    print('{} % {} = {}'.format(a,b, a % b))
    
    print('divmod({},{}) = {}'.format(a,b,divmod(a,b)))
    res,rem = divmod(a,b)
    t = divmod(a,b)
    print('res={},rem={}'.format(res,rem))
    print('type t {} type t[1] {}'.format(type(t), type(t[1])))
    
    a,b = b,a
    
    c = 2
    d = 2
    
    print('c is d ->', c is d)
    print('c == d ->', c == d)
    
    tp = (1,2,3)
    lp = (1,2,3)
    print('tp is lp', tp is lp)
    print('id of tp {}  id of lp {}'.format(id(tp),id(lp) ) )
    cp = tp
    print('tp is cp', tp is cp)
    print('id of tp {}  id of cp {}'.format(id(tp),id(cp) ) )
    
    a = 2
    b = a
    c = b
    #a = 3
    print('a {} b {} c {} '.format(id(a),id(b),id(c)))
    
    ls = [1,2,3]
    ts = ls.copy()
    #ts = ls #Ref
    print('ls is ts->', ls is ts)
    