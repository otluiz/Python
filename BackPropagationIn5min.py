#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import numpy as np
#from sklearn.svm import SVR
#import matplotlib.pyplot as plt

X = np.array([[0,0,1], [0,1,1], [1,0,1], [1,1,1]])
Y = np.array([[0], [1], [1], [0]])

np.random.seed(123456)

## criando e inicializando pesos
## obs: o produto da matriz (3x4) com a 
## matriz (4x1) resulta numa matriz (3x1)
peso0 = 2*np.random.random((3,4)) - 1
peso1 = 2*np.random.random((4,1)) - 1

## imprime os pesos a titulo de conferência
#print(peso0)
#print(peso1)

## função de ativação
def nonlin(x,deriv=False):
    if(deriv==True):
       return x*(1-x)
    return 1/(1+np.exp(-x))

## conjunto de treinamento
for j in range(6000000):
  ### feed forward through layer 0, 1, 2
  layer0 = X
  layer1 = nonlin(np.dot(layer0, peso0))
  layer2 = nonlin(np.dot(layer1, peso1))

  ## calcula o erro
  layer2_erros = Y - layer2
  if (j % 10000) == 0:
     print("Erro: "+str(j/10000)+ " = " + str(np.mean(np.abs(layer2_erros))))

  ## Back propagation dos erros usando a derivada regra da cadeia
  layer2_delta = layer2_erros*nonlin(layer2, deriv=True)
  layer1_erros = layer2_delta.dot(peso1.T)
  layer1_delta = layer1_erros*nonlin(layer1, deriv=True)

  ## usando o delta, podemos usar quando atualizar os pesos para reduzir
  ## as taxas de erros sempre com iterações
  ## Esse algotimo é chamado de gradiente descendente
  peso1 += layer1.T.dot(layer2_delta) *.1 ## nossa taxa de aprendizado
  peso0 += layer0.T.dot(layer1_delta) *.1 ## nossa taxa de aprendizado

