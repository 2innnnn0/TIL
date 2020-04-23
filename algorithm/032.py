# 032.py
# 32번 - 단어갯수 세는 프로그램
word = input()
word_list = list(word.split(' '))
print(len(word_list))

import pandas as pd

list_keys = ['a', 'b']
list_values = [['x', 'y'], [1, 2]]

list( zip(list_keys, list_values) )

x='banana'
dir(x)

x.count('a')

lst = [1,2,3,4]

lst_iter = iter(lst)
lst_iter
next(lst_iter)


#
import logging

logging.info('info test')
logging.warning('warning')
logging.error('error')

