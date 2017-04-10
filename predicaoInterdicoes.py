#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt

dia = []
br  = []
km  = []
mun = []
vis = []
tip = []
pis = []
via = []
hor = []



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
    return combo


# recebe uma lista de strings do tipo: ('5/2/2015 08:55', '20/1/2015 10:10', '5/1/2015 11:28')
# retorna uma lista de datetime no vetor dia
def converteDateTime(lista):
    dia = [trataDataHora(quebraData(i[0:15])) for i in dia]
    return dia



def get_data(filename):
    with open(filename, 'r') as csvfile:
         csvFileReader = csv.reader(csvfile)
         next(csvFileReader)
         for row in csvFileReader:
             dia.append(converteDateTime(row[0]))
             br.append(row[1])
             km.append(float(row[2]))
             mun.append(row[3])
             vis.append(row[4])
             tip.append(row[5])
             pis.append(row[6])
             via.append(row[7])
             hor.append(row[8])
    return



# altera o vetor dia[] para tipo datetime
#dia = converteDateTime(dia)


def predict_acidentes(dia, br, x):
    #dates = np.reshape(dates,(len(dates), 1))

    svr_lin = SVR(kernel= 'linear', C=1e3)
    svr_poly= SVR(kernel= 'poly', C=1e3, degree = 2)
    svr_rbf = SVR(kernel= 'rbf' , C=1e3, gamma=0.1)
    svr_lin.fit(dia, br)
    svr_poly.fit(dia, br)
    svr_rbf.fit(dia, br)

    plt.scatter(dia, br, color='black', label='Data')
    plt.plot(dia, svr_rbf.predict(dia), color='red', label='RBF_model')
    plt.plot(dia, svr_lin.predict(dia), color='green', label='Linear_model')
    plt.plot(dia, svr_poly.predict(dia), color='blue', label='Polynomial_model')
    plt.xlabel('Data')
    plt.ylabel('br')
    plt.title('Suport Vector Regression')
    plt.legend()
    plt.show()

    return svr_rbf.predict(x)[0], svr_lin.predict(x)[0], svr_poly.predict(x)[0]

#Arquivo entrada
get_data("/home/otluiz/workspace/python/Dados/prfInterdicoes.csv")

predited_ = predict_acidentes(dia, br, 1)

print(predicted_)
