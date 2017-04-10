#!/usr/bin/python
# -*- coding: utf-8 -*-
#Script python para gravar as dua primeiras colunas do csv

import sys
import csv
import numpy as np
from datetime import datetime, date, time

dia = []
br  = []
km  = []
mun = []
vis = []
tip = []
pis = []
via = []
hor = []


def get_data(filename):
    with open(filename, 'r') as csvfile:
         csvFileReader = csv.reader(csvfile)
         next(csvFileReader)
         for row in csvFileReader:
             dia.append(row[0])
             br.append(row[1])
             km.append(row[2])
             mun.append(row[3])
             vis.append(row[4])
             tip.append(row[5])
             pis.append(row[6])
             via.append(row[7])
             hor.append(row[8])
    return

# recebe uma string tipo data '23/12/2010 18:24'
# retorna uma lista de string ('23/12/2010', '18:24')
def quebraData(datahora):
    parteDH = datahora.split(' ')
    return (parteDH[0], parteDH[1])


# recebe uma lista de string ('23/12/2010', '18:24')
# e converte em ditetime para o python
def trataDataHora(datahora):
    parteD = datahora[0].split('/')
    parteH = datahora[1].split(':')
    novoD  = date(int(parteD[2]), int(parteD[1]), int(parteD[0]))
    novoH  = time(int(parteH[0]), int(parteH[1]))
    combo  = datetime.combine(novoD,novoH)
   #datahora = datetime.strptime(hora, '%h:%m')
   #print (combo)
    return combo


# recebe uma lista de strings do tipo: ('5/2/2015 08:55', '20/1/2015 10:10', '5/1/2015 11:28')
# retorna uma lista de datetime no vetor dia
def converteDateTime(listaDataHora):
    data = [trataDataHora(quebraData(i[0:15])) for i in dia]
    return data

#Arquivo entrada
get_data("/home/otluiz/Mestrado/DadosPRF/DadosSaida/prfInterdicoes.csv")

# altera o vetor dia[] para tipo datetime
dia = converteDateTime(dia)
