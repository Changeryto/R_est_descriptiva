# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 19:50:53 2021

@author: ruben
"""

import matplotlib.pyplot as plt

import numpy as np

# Diagrama de cajas y bigotes

np.random.seed(19880519)

dist1 = 100 * np.random.rand(50) #no aleatorio entre 0 y 100

dist2 = 50*np.ones(25)

dist3 = np.random.rand(10) * 100 + 100

dist4 = -100 * np.random.rand(10)



data = np.concatenate((dist1, dist1, dist2, dist3, dist4))

fig1, ax1 = plt.subplots()
ax1.set_title("Boxplot básico")
ax1.boxplot(data)
plt.show()

# Parámetros importantes


## Boxplot con muescas

fig2, ax2 = plt.subplots()
ax2.set_title("Boxplot con notch")
ax2.boxplot(data, notch = True)
plt.show()

## Boxplot con outliers de diamantes

green_diamond = dict(markerfacecolor = "green",
                 marker = "D")
fig3, ax3 = plt.subplots()
ax3.set_title("Boxplot de outliers personalizados")
ax3.boxplot(data, flierprops=green_diamond)
plt.show()


## Boxplot en horizontal

red_sq = dict(markerfacecolor = "red",
              marker = "D")
fig4, ax4 = plt.subplots()
ax4.set_title("Boxplot en horizontal")
ax4.boxplot(data, vert = False, flierprops = red_sq, showfliers = True)
plt.show()


## Boxplot sin outliers

fig5, ax5 = plt.subplots()
ax5.set_title("Boxplot sin outliers")
ax5.boxplot(data, showfliers = False, vert = True)
plt.show()

## Boxplot con bigotes personalizados



fig6, ax6 = plt.subplots()
ax6.set_title("Boxplot de bigotes personalizados")
ax6.boxplot(data, whis = 0.75) # Número de veces del rango intercuartílico
plt.show()


## Múltiples boxplot


dist1 = 100 * np.random.rand(50) #no aleatorio entre 0 y 100

dist2 = 40*np.ones(25)

dist3 = np.random.rand(10) * 100 + 100

dist4 = -100 * np.random.rand(10)


data2 = np.concatenate((dist1, dist1, dist2, dist3, dist4))



data.shape = (-1,1)
data2.shape = (-1,1)

fulldata = [data.flatten(), data2.flatten(), data2[::2,0].flatten()]

fig7, ax7 = plt.subplots()
ax7.set_title("Múltiples muestras de diferente naturaleza")
ax7.boxplot(fulldata)
plt.show()









