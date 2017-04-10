#!/usr/bin/env python
# _+_ coding: utf-8 _+_

# testa de herança encadeada

class B:
	pass

class C(B):
	pass

class D(C):
	pass

for c in [D, C, B]:
	try:
	   raise c()
	except D:
	   print "D"
	except C:
	   print "C"
	except B:
	   print "B"
