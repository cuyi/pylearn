#! /usr/bin/env python2.7
# -*- coding:utf8 -*-

# define a function: fib(n)
# this function write Fibonacci series up to n
def fib(n):
    a, b = 0, 1
    while a < n:
        print a,
        a, b = b, a+b

# Now we call the fib(n) we just defined:
fib(3000)
