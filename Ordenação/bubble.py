# Algoritmo de ordenação
## Bubble sort

import random
import numpy as np

def bubble(vetor):
    n = len(vetor)

    for i in range(n):
        for j in range (0, n-i-1):
            if vetor[j] > vetor[j + 1]:
                temp = vetor[j]
                vetor[j] = vetor[j + 1]
                vetor[j + 1] = temp
    return vetor

result = random.sample(range(0,100),20) ## gera 20 número aleatorios

print(result)

print(bubble(result))
