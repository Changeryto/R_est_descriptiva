# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 19:14:00 2021

@author: ruben
"""

import seaborn as sb

planets = sb.load_dataset("planets")

print("Dimensiones:",planets.shape)

print(planets.head)


# Aparentemente dropna() descarta toda fila con NA

print("Descripción: \n",planets.dropna().describe())

import pandas as pd

print("\n Suma de la distancia:", planets.distance.sum())

print("\n Producto de la distancia:", planets.distance.prod())



# (sumatorio de : x_i - media: )  / n

print("\n MAD:", planets.distance.mad())


print("\n Desv. est. de la distancia:", planets.distance.std())


## Agrupando por método



pgm = planets.groupby("method")["orbital_period"].median()

print("\n Medias del periodo orbital según el método:", pgm)

print("\n\n\n Para cada elemento qué métodos forman parte de dicho grupo \n")

## Hacer iteraciones sobre los métodos

for (method, group) in planets.groupby("method"):
    print("{0:30s} shape={1}".format(method, group.shape))



# Describir para cada método como se comporta la variable de años

myd = planets.groupby("method")["year"].describe()

print("\n Para cada método como se comporta la variable de años", myd)



# Clasificando los planetas descubiertos por método y década de descubrimiento.

decade = 10 * (planets["year"] // 10)

decade = decade.astype(str)+"s"

decade.name = "decade"

pmnd = planets.groupby(["method", decade])["number"].sum()

print("Décadas de descubriiento:", pmnd.unstack().fillna(0)) ## Cambiar NA por 0

