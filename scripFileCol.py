#!/usr/bin/python
# -*- coding: utf-8 -*-
#Script python para gravar as dua primeiras colunas do csv

f=open("/home/otluiz/workspace/python/PRF_Dic.csv","r")
g=open("/home/otluiz/workspace/python/Dic.csv","w")
for lin in f:
 col=lin.split(",")
 col[4]
 col[5] 
jun=",".join(col)
g.write(jun)
g.close()
f.close()
