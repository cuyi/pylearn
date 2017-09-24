#! /usr/bin/env python2.7
# -*- coding:utf8 -*-

# The defualt vaules are evaluated at the point of the function definition
# in the defining scope.
i = 5;
def f(arg = i):
    print arg

i = 6
# the following code will print 5
f()


''' default value is evaluated only once. This makes 
a difference when the defualt is a mutable object such as:
list, dictionary, instances of most classes '''
def f(a, L = []):
    L.append(a)
    return L

print f(1)
print f(2)
print f(3)

''' To avoid above questions, we can do like bellows: '''
def f1(a, L = None):
    if(L is None):
        L = []
    L.append(a)
    return L

print f1(1)
print f1(2)
print f1(3)


