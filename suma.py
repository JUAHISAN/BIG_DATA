import pyspark
from pyspark import SparkContext
import time

sc = SparkContext()

inicio = time.time()
#numeros = sc.parallelize(range(1000000))
#numeros_sc = sc.parallelize([1,2,3,4,5,6,7,8,9,10])
#sum_numeros = numeros.map(lambda a: a+10).collect()
#print(sum_numeros)

numeros_2 = range(1000000)
lista = list()

for i in numeros_2:
    a = i+10
#    #print (a)
    lista.append(a)

#print(lista)


fin = time.time()
print("Total tiempo ejecución {}".format(fin-inicio)) 
