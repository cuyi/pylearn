#! /usr/bin/env python2.7
# -*- coding:utf8 -*-

a = ['cat', 'window', 'defenestrate']
for x in a:
    print x, len(x)


# It is not safe to modify the sequence being iterated over in the loop.
# So we MUST iterate over a copy.
# The slice notation makes this particularly convenient.
for x in a[:]: # make a slice copy of the entire list
    if len(x) > 6:
        a.insert(0, x)

print a


