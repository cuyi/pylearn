#! /usr/bin/env python2.7
# -*- coding:utf8 -*-

# define a function: fib(n)
# this function write Fibonacci series up to n
def fib(n):
    a, b = 0, 1
    while a < n:
        print a,
        a, b = b, a+b

'''
A function definition introduecs the function name in the current symbol table
函数的定义会在当前符号表中引入这个函数名,
The value of the function name has a type, 被解释器认为是 user-defined function
这个值可以赋值给另外一个名字，这个另外的名字也可以当作函数使用，这就为函数重命名提供了一种机制
'''
print fib


# Now we call the fib(n) we just defined:
fib(3000)
print

''' 
    Some thing about function execution

一个函数的执行会引入一个新的符号表用于该函数的局部变量。
更确切的说是函数中所有变量的赋值都将值存储在局部符号表中。
变量的索引查找的顺序是：
    1. local symbol table（局部符号表）
    2. local symbol tables of enclosing functions（闭包函数的局部符号表）
    3. global symbol talbe（全局符号表）
    4. table of built-in names
'''

def calc_half_of_a_num(x):
    print int(x)/2

calc_half_of_a_num(9)

