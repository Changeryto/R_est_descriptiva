# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 23:31:38 2022

@author: ruben
"""

# Una técnica es tomar una parte de los datos (0.8) para fabricar el modelo
# Y el resto para validar los datos
# Permite evitar el overfiting
# Se suele seguir la regla del 80 20


import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

diabetes = datasets.load_diabetes()

mod = linear_model.LinearRegression()

x = diabetes.data[:, np.newaxis, 2] #Selecciona sólo la primera columna

y = diabetes.target





x_train = x[:-60] #Todas las filas excepto las últimas 60
x_test = x[-60:] #De las últimas 60 en adelante

y_train = y[:-60]
y_test = y[-60:]






plt.scatter(x_train, y_train, color="black")

mod.fit(x_train, y_train)
plt.plot(x_train, mod.predict(x_train), color="blue", linewidth=3)
plt.show()

print("C")
print("Ordenada al origen", mod.intercept_)

print("R^2", r2_score(y_train, mod.predict(x_train)))


## Testing

y_pred = mod.predict(x_test)
print("\nError cuadrado medio:",mean_squared_error(y_test, y_pred))
# En comparación con el anterior 3890, se concluye que este modelo no tiene problemas de overfitting


print("\ntest vs pred", r2_score(y_test, y_pred))


plt.scatter(x_train, y_train, color="black")
plt.scatter(x_test, y_test, color="red")
mod.fit(x_train, y_train)
plt.plot(x_train, mod.predict(x_train), color="blue", linewidth=3)
plt.show()



