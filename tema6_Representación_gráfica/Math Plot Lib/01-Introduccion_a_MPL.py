# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 00:26:07 2021

@author: ruben
"""

import matplotlib.pyplot as plt
import numpy as np

y = [1, 2, 3, 4]

#Cuando sólo se da un vector de datos, se toma
# como datos de Y

#Segmento contínuo
plt.plot(y)
plt.xlabel("Eje de abscisas")
plt.ylabel("Eje de ordenadas")
plt.show()

# Puntos discretos

x = [1, 2, 3, 4]
y = [1, 4, 9, 16]
plt.plot(x, y, 'ro') #red y circulo
plt.axis([0, 6, 0, 20]) #x de 0 a 6 / y de 0 a 20
plt.show()


data = np.arange(0.0, 10.0, 0.2)
plt.plot(data, data, "r--") #Guionsitos
plt.show()



plt.plot(data, data, "r--",
         data, data**2, "bs",
         data, data**3, "g^")
plt.show()


# ### Parámetros

# linewidth: tamaño de las líneas

plt.plot(y, linewidth = 20)
plt.show()

# antialisaing

linea = plt.plot(y)

#linea.aa(False)
plt.show()

# setp

linea2 = plt.plot(data, data, data, data**2)
plt.setp(linea2, color = "r", linewidth = 2.0)
plt.show(linea2)

# alpha

plt.plot(x, y, alpha = 0.5)

# marker

plt.plot(x, x, marker = "+", linestyle = ":")

# animated

plt.plot(x, x, marker = "+", linestyle = ":", animated = True)


plt.setp(linea)
