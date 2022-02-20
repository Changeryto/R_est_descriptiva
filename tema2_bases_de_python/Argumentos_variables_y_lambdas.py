import math

def suma(*argumento_de_longitud_variable):
    return sum(argumento_de_longitud_variable)


suma_de_varios_numeros = suma(10, 47, 8)
print(suma_de_varios_numeros)

def suma_de_cuadrados(*datos):
    total = 0
    for d in datos:
        total += d**2
    return total
        
print(suma_de_cuadrados(2, 4, 6))

#Funciones anónimas o funciones lambdas

#se usa lambda en lugar de def

#Más similar a R donde:
#doble = function(x){x ** 2}

doble = lambda x: x * 2

print(doble(5))

#Lambda es útil para filtrar datos, mapear y resumir


from functools import reduce

#Filtrar datos
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

filtered_data = list(filter(lambda x : (x * 2  > 8), data))
#Ha filtrado en filter con un lambda, todo número de un argumento iterable
#que al multiplicarse por dos sea mayor que 8, y lo coloca en una lista

print(filtered_data)


#Mapear datos
mapped_data = list(map(lambda x: x*2, data))
#Enlista con la función map las partes de un iterable data pasadas por la función lambda

print(mapped_data)


#Reducir datos
reduced_data = reduce(lambda x, y: x + y, data)
#Dado el resultado anterior x, suma el nuevo y; el primer x es 0
#El primer y es el index 0
'''
print(data[0])
print(data[-1])
data.pop(0)
print(data)
'''