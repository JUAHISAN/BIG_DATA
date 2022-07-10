import pyspark
from pyspark import SparkContext

sc = SparkContext()

numeros = sc.parallelize([1,2,3,4,5,6,7,8,9,10])
sum_numeros = numeros.map(lambda a: a+10).collect()
print(sum_numeros)

numeros_2 = [1,2,3,4,5,6,7,8,9,10]
lista = list()

for i in numeros_2:
    a = i+10
    print (a)
    lista.append(a)

print(lista)