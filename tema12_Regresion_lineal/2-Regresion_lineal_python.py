# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 23:08:33 2022

@author: ruben
"""


import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score


## Regresión lineal de la Diabetes

diabetes = datasets.load_diabetes()

print(type(diabetes), "\n")

print(type(diabetes.data), "\n")

print(diabetes.data.shape, "\n")

x = diabetes.data[:, np.newaxis, 2] #Selecciona sólo la primera columna

y = diabetes.target


#Creando el modelo de datos

mod = linear_model.LinearRegression()
mod.fit(x, y) #Calcula los coeficientes de la regresión

print(mod.coef_, "Coeficiente de las x\n") #Coeficiente de las x

print(mod.intercept_, "Ordenada al origen\n") #Ordenada al origen

plt.scatter(x, y, color = "black")
plt.plot(x, mod.predict(x), color="blue", linewidth=3)
plt.show()


## Coeficiente

print(mean_squared_error(y, mod.predict(x)), "Error cuadrado medio \n")

# $$MSE = \frac{\sum{(y_i - \tilde{y_i})^2}}{n}$$

print(r2_score(y, mod.predict(x)), "R^2 \n") #Demasiada dispersión













