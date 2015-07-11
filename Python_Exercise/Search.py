#!/usr/bin/env python
# coding:utf-8
author='Jerry Zhong'

import os
import sys
def search(str,dir):
	if dir.startswith('~'):
		dir=dir.replace('~','/home/jerry')
	for d in os.listdir(dir):
		if os.path.isfile(os.path.join(dir,d)) and str in d:
			print os.path.join(dir,d)
		elif os.path.isdir(os.path.join(dir,d)):
			search(str,os.path.join(dir,d))
if __name__=='__main__':
	if len(sys.argv)==3:
		search(sys.argv[1],sys.argv[2])
	else:
		print 'wrong argument number,it should be 2'
