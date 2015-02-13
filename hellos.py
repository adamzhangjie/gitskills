#!/usr/bin/env python
# _*_ coding: utf-8 _*_

' a test module '

__author__ = 'Adam Zhang'

import sys

def test():
	args = sys.argv
	if len(args)==1:
		print 'Hello, World!'
	elif len(args)==2:
		print 'Hello, %s!' % args[1]
	else:
		print 'Too manay arguments!'

def _private_1(name):
    print 'Hello, %s' % name

def _private_2(name):
	print 'Hi, %s' % name

def greeting(name):
	if len(name) > 3:
		return _private_1(name)
	else:
		return _private_2(name)


if __name__ == '__main__':
    test()
    print 'Something done'
    greeting('Ad')
else:
    print 'noThing to do'
    greeting('Adam')