# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 20:45:11 2021

@author: ruben
"""
import numpy as np
import matplotlib.pyplot as plt

class Fun:
    
    def __init__(self, rango = 0):
        self.rango = rango
    
        
    @classmethod  
    def prof(cls, rango):
        cls.rango = rango
        return np.exp(-cls.rango)*np.cos(2*np.pi*cls.rango)


x1 = np.arange(0, 5.0, 0.1)
x2 = np.arange(0, 5.0, 0.2)

# Con 1 fila y una columna
plt.plot(x1, Fun.prof(x1), "ro", x2, Fun.prof(x2), "k")
plt.show()

### Dos filas y una columna
plt.figure(1) #Opcional para una figura, 1 por defecto
plt.subplot(2, 1, 1) # Filas = 2; Columnas =1; usadas para representar
plt.plot(x1, Fun.prof(x1), "ro", x2, Fun.prof(x2), "k")
plt.subplot(2, 1, 2) # Filas y columnas del segundo
plt.plot(x2, Fun.prof(x2), "g--")
plt.show()

### 
plt.figure(1)
plt.subplot(2, 1, 1)
plt.plot([1, 2, 3])
plt.subplot(2, 1, 2)
plt.plot([4, 5, 6], "r")

plt.figure(1)
plt.subplot(2, 1, 1)
plt.title("Este es el primer título")

plt.subplot(2, 1, 2)
plt.title("Este es el segundo título")
plt.show()
