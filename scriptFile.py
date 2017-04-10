#!/usr/bin/python 
#Script python para gravar 2 colunas do arquivo prf.csv
import io
#from __future__ import unicode_literals


with io.open(r"/home/otluiz/Mestrado/Dados_PRF/DadosEntrada/prf.csv", "r", encoding="utf-8") as f1:
     with io.open(r"/home/otluiz/Mestrado/Dados_PRF/DadosSaida/prfSaida.csv", "w", encoding="utf-8") as f2:
        for lin in f1:
          s1=lin[0:len(lin)]
          s2=lin.split(",")
          s2[0]
          s2[1]
          s3=";".join(s2)
          f2.write(s3)
f2.close()
f1.close()
