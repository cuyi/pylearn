#! /usr/bin/env python2.7
# -*- coding:utf8 -*-

# raw_input([prompt])
# The function then reads a line from input, 
# converts it to a string (stripping a trailing newline), and returns that.

x = int(raw_input("Please input an integer: "))

if x < 0:
    x = 0
    print 'Negative changed to zero'
elif x == 0:
    print 'Zero'
elif x == 1:
    print 'Single'
else:
    print 'More'

