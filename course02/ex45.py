'''
Created on Jul 15, 2016

@author: wizard
'''
import re
   
if __name__ == '__main__':
    text = r'''
drwxrwxr-x  4 wizard wizard      4096 яну 18  2018 robo3t-1.1.1
drwxrwxr-x  4 wizard wizard      4096 юни 27 16:24 robo3t-1.2.1
-rw-rw-r--  1 wizard wizard        44 окт 29 10:05 sdb1.uuid
drwxrwxr-x  2 wizard wizard      4096 авг 25  2017 sh_folder
'''
    result = re.findall(r'(\w{3})\s{1,2}(\d{1,2})\s{1,2}(\d{4}|\d{2}:\d{2})',text)
    print(result)