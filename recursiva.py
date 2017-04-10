#! /usr/bin/env python
# -+- coding: utf-8 -*-

class Recursiva(object):

        def recursiva(self, n):
                if n == 1 : return 1
                else : return (n + recursiva(n -1))

print ("Soma de %d e soma de %d", recursiva(3), recursiva(5))
    
