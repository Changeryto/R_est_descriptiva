# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 00:26:02 2021

@author: ruben
"""

import matplotlib.pyplot as plt
import numpy as np
from mgpf import Fun
# Si xlabel deja de funcionar ---
# from imp import reload
# reload(plt)

r = np.arange(0, 100, 2)

cord = Fun.prof(r)

plt.plot(cord, "r--")
plt.ylabel("Eje Y")
plt.xlabel("Eje X")
plt.show()

# Histograma de frecuencias de dist normal

mu = 100
sigma = 20

x = mu + sigma * np.random.randn(10000)

n, bins, patches = plt.hist(x, 50, density=1, facecolor="g", alpha=0.6)
plt.xlabel("Cociente intelectual", color="green")
plt.ylabel("Probabilidad")
plt.title(r"Histograma de CI $N(\mu, \sigma)$")
plt.text(120, 0.015, r'$\mu = 100,\ \sigma = 20$') #En latex MD
plt.axis([20, 180, 0, 0.025])
plt.grid(True) #Para colocar parrilla
plt.figure(figsize = (10, 6), dpi=300) #size En pulgadas
plt.subplot(1, 1, 1) #Tecnicamente no necesario

x = np.arange(0, 10*np.pi, 0.01)
y = np.cos(x)
plt.plot(x, y, lw=2.0)
plt.annotate("Máximo local", xy=(4*np.pi, 1), xytext=(15, 1.5),
             arrowprops=dict(facecolor="black", shrink=0.05)) #shrink cambia longitud de flecha
plt.ylim(-2, 2)

plt.show()



