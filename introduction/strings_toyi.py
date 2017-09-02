#! /usr/bin/env python2.7
# -*- coding: utf8 -*-

mstr = 'hello qianjie'
print mstr

mmstr = 'hello piaoliang\n\
what r u nong sa li?'
print mmstr

hello = '''This is a rather long
    string containing several lines of text.'''
print hello

hello1 = """This is a rather long
    string containing several lines of text."""
print hello1

# Strings can be concatenated with the + operator, and repeated with *
word = 'Help' + 'Poor Yi'
print word
print word*5

# Strings can be subscripted (indexed)
print word[0]
print word[0:2]

# Unlike a C string, Python strings cannot be changed.
# The following code is WRONG
# word[0] = 'x'

# built-in function len() returns the length of a string:
s = 'I love you: qian jie'
print len(s)
