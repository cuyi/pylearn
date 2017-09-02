#! /usr/bin/env python2.7
# -*- coding:utf8 -*-

''' 循環語句可以有一個else 語句：
    這個else語句執行的前提是for語句遍歷完了list或者是while的條件變爲false
    但當該層loop被beak終結時，else是不會被執行的。
    
    即可以理解爲這個else語句跟for是一起的，break的時候這個else也被break跳出了
'''

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print n, 'equals', x, '*', n/x
            break
    else:
        print n, 'is a prime number'
