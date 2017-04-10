#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, date, time


d  = '26/2/2010'
h   = '18:24'

def trataDataHora(d, h):
    parteD = d.split('/')
    parteH = h.split(':')
    novoD  = date(int(parteD[2]), int(parteD[1]), int(parteD[0]))
    novoH  = time(int(parteH[0]), int(parteH[1]))
    combo  = datetime.combine(novoD,novoH)
   #datahora = datetime.strptime(hora, '%h:%m')
    print (combo)

