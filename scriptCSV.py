#!/home/otluiz/python3.5/Python-3.5.1/python 
#Script python para gravar 2 colunas do arquivo prf.csv
import csv

cr=csv.reader(open("/home/otluiz/workspace/python/PRF_Dic.csv","r"))
c = csv.writer(open("/home/otluiz/workspace/python/dicPRF.csv", "w"))

for lin in cr:
 c.writerow([lin[2]]+ [lin[3]]+[lin[4]]+ [lin[5]])


