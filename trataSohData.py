#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import date
d  = '06/12/2010'
#hora    = '18:24'
partes = d.split('/')
novod  = date(int(partes[2]), int(partes[1]), int(partes[0]))

#datahora = datetime.strptime(hora, '%h:%m')
print (novod)
