'''
Created on Jul 15, 2016

@author: wizard
'''

   
if __name__ == '__main__':
    #with open('output.txt','w') as fh:
    #    print('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed', file=fh)
    try:
        with open('output.txt','x') as fh:
            print('Consectetur adipisicing elit, sed do eiusmod', file=fh)
    except FileExistsError as e:
        print(e)    