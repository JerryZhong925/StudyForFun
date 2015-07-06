#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'a test module'

__author__='Jerry Zhong'

import sys
def _test_1():
	args=sys.argv
	if len(args) == 1:
		print("HELLO")
	elif len(args) == 2:
		print("HELLO",args[1])
	else:
		print("TOO MUCH",agrs[0])
def test():
	print('hi')
if __name__ =='__main__':
	test()
