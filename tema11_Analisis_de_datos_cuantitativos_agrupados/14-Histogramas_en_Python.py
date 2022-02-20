# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 23:49:15 2022

@author: ruben
"""

# Histogramas en Python

## Vanilla

x = (0,1,1,1,2,2,3,7,7,7,25)

def count_elements(seq) -> dict:
    """Función que cuenta las frecuencias
    de aparición de cada elemento de la 
    secuencia creando un diccionario como
    si fuese una tabla de frecuencias"""
    
    hist = {}
    for i in seq:
        hist[i] = hist.get(i, 0) +1
    return hist


fAbs = count_elements(x)

print(fAbs)


## Con Collections

from collections import Counter
fAbs2 = Counter(x)

print(fAbs2)

def ascii_histogram(seq) -> None:
    """Un histograma de frecuencias absolutas
    colocado en horizontal y con caracteres ASCII"""
    fAbs = count_elements(seq)
    for k in sorted(fAbs):
        print("{0:5d} {1}".format(k, "+"*fAbs[k]))
        

ascii_histogram(x)

print("\n\n")

import random
random.seed(2019)

vals = [1,2,3,5,7,8,9,10]
freqs = (random.randint(5,20) for _ in vals)

data = []
for k, v in zip(vals, freqs):
    data.extend([k]*v)

ascii_histogram(data)
    
print("\n")
    


## Histogramas con NumPy

import numpy as np

np.set_printoptions(precision=3)

x = np.random.laplace(loc=10, scale=3, size=1000)

hist, bin_edges = np.histogram(x)

print("\n", hist)
print("\n", bin_edges)

print("\n",hist.size, bin_edges.size) #Esto es igual

min_edge = x.min()
max_edge = x.max()

n_bins = 10
bin_edges = np.linspace(start=min_edge, stop=max_edge, num=n_bins+1, endpoint=True)

print("\n", bin_edges) #A esto

x = (0,1,1,1,2,2,3,7,7,7,25)
bcount = np.bincount(x) #Cuenta las frecuencias de los enteros implicados

hist, _ = np.histogram(x, range=(0, max(x)), bins = max(x)+1)

print("\n", hist)
    
np.array_equal(bcount, hist)

print("\n",dict(zip(np.unique(x), bcount[bcount.nonzero()])))

    

## Histogramas con MatPlotLib y Pandas

import matplotlib.pyplot as plt

x = np.random.laplace(loc=10, scale=3, size=1000)

n, bins, patches = plt.hist(x = x, bins=int(np.sqrt(len(x))), color = "#0505a5", alpha = 0.75, rwidth = 0.85)
plt.grid(axis="y", alpha=0.5)
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.title("Un hstograma de frecuencias")
plt.text(-10, 80, r"$\mu = 10, b = 3$")

#plt.ylim(ymax=np.ceil(maxfreq/10)*10 if maxfreq%10 else maxfreq +10)

plt.show()

#bins contiene los extremos, patches la lista de 58 objetos


import pandas as pd

size, scale = 1000, 10
data = pd.Series(np.random.gamma(scale, size = size))

data.plot.hist(grid=True, bins=int(np.sqrt(len(x))), rwidth = 0.9, color="#d52675")
plt.title("Distribución Gamma")
plt.xlabel("Valores")
plt.ylabel("Frecuencias")
plt.grid(axis = "y", alpha = 0.75)





## Funciones de densidad y de probabilidad

mu = 10, 20

sigma = 5, 2

dist = pd.DataFrame(np.random.normal(loc = mu, scale = sigma, size = (1000, 2)), columns=["x1", "x2"])

print("\n",dist.agg(["min", "max", "std"]).round(decimals = 2))

# Función de densidad estimada

fig, ax = plt.subplots()
dist.plot.kde(ax=ax, legend=False, title = "Histograma de ds normales")
dist.plot.hist(density = True, ax=ax) 
ax.set_ylabel("Probabilidad")
ax.grid(axis="y", alpha=0.75)
ax.set_facecolor("#d5d5d5")

plt.show()



from scipy import stats

dist = stats.norm()# Distribución normal teórica
 #N(0,1) = exp(-x**2/2)/sqrt(2*pi)

sample = dist.rvs(size = 1000)

x = np.linspace(start=stats.norm.ppf(0.01), stop=stats.norm.ppf(0.99))

gkde = stats.gaussian_kde(dataset=sample)

fig, ax=plt.subplots()
ax.plot(x, dist.pdf(x), linestyle = "solid", c="red", lw=3, alpha = 0.8, label="Distribución normal teórica")

ax.plot(x, gkde.evaluate(x), linestyle = "dashed", color="green", lw=2, label="PDF estimada con KDE")
ax.legend(loc="best", frameon=False)
ax.set_title("Normal analítica vs estimada")

ax.set_ylabel("Probabilidad")
ax.text(-2, 0.35, r"$f(x) = \frac{e^{x^{2/2}}}{\sqrt{2 \pi}}$")


## Otro método para representar histogramas con Seaborn

import seaborn as sb

sb.displot(data)


x = np.random.laplace(loc=10, scale=3, size=1000)
sb.set_style("darkgrid")
sb.displot(x, kde=True)


sb.distplot(data, fit=stats.laplace, kde=False)



## Más ejemplos con Pandas

data2 = np.random.choice(np.arange(10), size=10000, p=np.linspace(1, 11, 10)/60)
s = pd.Series(data2)
print("\n", s.value_counts(normalize=False))

print("\n", s.value_counts(normalize=True))

ages = pd.Series([1,1,3,5,6,8,9,10,12,15,18,18,20,25,30,40,51,52])
bins = (0,10,15,18,21,np.inf)
labels = ("Infancia", "pubertad", "adolecencia", "joven", "adulto")
groups = pd.cut(ages, bins=bins,labels = labels) #Igual al cut de R
print("\n",groups.value_counts())

### Data frame creado
print("\n", pd.concat((ages, groups), axis=1).rename(columns={0:"age", 1:"group"}))





