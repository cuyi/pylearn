#! /usr/bin/env python2.7
# -*- coding: utf8 -*-

# this is comment

import math

# The equal sign('=') is used to assign a value to a variable
# Variable MUST be "defined" (assign a value) before can be used
a = 4
print a

# The following is wrong bcz of b is not "defined"
# print b

# complex number
c = 1.8 + 8.9j
print c
print c.real
print c.imag

print abs(c)    # sqrt(c.real**2 + c.imag**2)
'''
from math import sqrt
print sqrt(c.real**2 + c.imag**2)
'''
# cmath or math is a module, these module provide access to the mathematical functions
from cmath import sqrt
print sqrt(c)
