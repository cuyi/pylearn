#! /usr/bin/env python2.7
# -*- coding:utf8 -*-

# List 可以用來將其它值放在一起，這些值用逗號隔開，且這些值可以有不同的類型
a = ['spam', 'eggs', 100, 1234]
print a

for e in a:
    print e


# List 與 string 不同的地方是，list中的每一個值（item）是可以改變的，而string中的值是不可以改變的
a[1] = 'lvlv'
a[2] = a[2] + 12
print a

# len() return the length (the number of items) of an object.
# The argument may be a sequence (string, list, tupe) or a mapping (dictionary)
print len(a)
