# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 21:00:50 2021

@author: ruben
"""

# Uso de NumPy
# Requiere usar datos homogeneos

# Ampliación del modulo de python

import numpy as np

#NumPy puede crear los objetos
# a partir de la lista

# En este caso un array

L1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

x1 = np.array(L1)

# Se puede especificar el tipo de dato
# usando "dtype = tipo"


# tipo = 'float32'
# Permite el generar la lista con valor decimal
x2 = np.array(L1, dtype = 'float32')
print(x2)

# tipo = 'bool'
# Listas de valores booleanos
x3 = np.array((L1 == 4), dtype = 'bool')
print(x3)

# tipo = 'int', 'intc', 'intp', 'int8', 'int16', 'int32', 'int64'
x4 = np.array(L1, dtype='int')
print(x4)


# tipo = 'uint', 'int8', 'uint16', 'uint32', 'uint64'
# Listas de enteros sin signo
x5 = np.array(L1, dtype='uint')
print(L1)

# tipo = 'float', 'float16/32/64" = half/omision/double
x6 = np.array(L1, dtype='float')
print(x6)

# tipo = 'complex', 'complex64/128'
#La mitd va para la real y la mitad para la imaginaria
# Complejos de 64 bits
x7 = np.array([3+4j, 8+1j], dtype='complex128')
print(x7)

# NumPy con matríz de 0
filas = 3
columnas = 4
n0 = np.zeros((filas, columnas))
print(n0)

# Matriz de 1
n1 = np.ones((filas, columnas))
print(n1)

# Matrices para crear listas de rangos que
# que crecen de forma regular
# similar al seq() de R

r = np.arange(10, 101, 5, dtype='float')
print(r)

# Linspace crea array con numero especificado de
# inicio y fin específico
# similar a seq(x, y, length=z)
rl = np.linspace(0, 5, num=10)
print(rl)


# Reordenar las marices constantes
print(n0.reshape(4, 3))


# Hacer matrices
m1 = np.array([L1, L1, L1])
print(m1)

# ravel nos permite aplanar el array
print(np.ravel(m1))
# usar ravel afecta el vector original


# flatten es una copia del array en una dimension
#print(np.flatten(m1))

# np.transpose cambia filas y columnas
print(np.transpose(m1))

# np.resize, igual que reshape
# pero empieza a rellenar las matrices
# de sobrar espacio

print(np.resize(m1, (6, 12)))




