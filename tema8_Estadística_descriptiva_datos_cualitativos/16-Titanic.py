# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 18:35:24 2021

@author: ruben
"""

#Datos del Titanic

import seaborn as sns
import pandas as pd
import numpy as np

titanic = sns.load_dataset("titanic")


print(titanic.head())
print(titanic.shape)


titanic['survived'] = pd.Categorical(titanic['survived'])

titanic['pclass'] = pd.Categorical(titanic['pclass'])

titanic['sex'] = pd.Categorical(titanic['sex'])

titanic['deck'] = pd.Categorical(titanic['deck'])

# Tabla de contingencias de una variable

tab = pd.crosstab(index = titanic["survived"],
                  columns = "pasajeros")

print(tab)
print(type(tab))

clase = pd.crosstab(index = titanic["pclass"],
            columns = "pasajeros por clase")

print(clase)



sexo = pd.crosstab(index = titanic["sex"],
            columns = "sexo del pasajero")

print(sexo)


cubierta = pd.crosstab(index = titanic["deck"],
            columns = "pasajeros por cubierta")


print(cubierta)

#Resumir datos

cubierta.sum()

cubierta.shape

cubierta.iloc[1:5]

# Como sacar frecuencias relativas

cubierta/cubierta.sum() #Ahora se tiene la proporción

# Proporción de hombres y mujeres

sexo/sexo.sum()

# Proporción de supervivientes

supervivencia = pd.crosstab(index = titanic["survived"], 
                            columns = "Supervivencia")

supervivencia/supervivencia.sum()


# Tablas para 2 variables

survived_sex = pd.crosstab(index = titanic["survived"],
                           columns = titanic["sex"])

## Cambiar nombres de las filas
survived_sex.index =["died", "survived"]

survived_class = pd.crosstab(index = titanic["survived"],
                             columns = titanic["class"])

survived_class.index = ["Murió", "Vivió"]
survived_class.columns = ["Primera", "Segunda", "Tercera"]


print(survived_class)


##Total por fila

survived_class2 = pd.crosstab(index = titanic["survived"],
                             columns = titanic["class"],
                             margins=True)

survived_class2.index = ["Murió", "Vivió", "Total_s"]
survived_class2.columns = ["Primera", "Segunda", "Tercera", "Total_c"]

print(survived_class2)



## Frecuencias relativas globales

survived_class2/survived_class2.loc["Total_s","Total_c"]

print(survived_class2/survived_class2.loc["Total_s","Total_c"])



## Frecuencias relativas marginales

# Ratio de supervivencia por clase (columna)

survived_class2/survived_class2.loc["Total_s"]

survived_class2.div(survived_class2.loc["Total_s"], axis=1)

# Ratio de supervivencia por condición (ex fila)

survived_class2.T/survived_class2["Total_c"]

# o conservando la fila
survived_class2.div(survived_class2["Total_c"],axis=0)


## Tablas multidimensionales

survived_sex_class = pd.crosstab(index = titanic["survived"],
                                 columns = [titanic["sex"], titanic["pclass"]],
                                 margins=True)

# Estraer la subtabla primero col1 y luego col2

survived_sex_class["female"][1]


# Marginal por col

survived_sex_class/survived_sex_class.loc["All"]
















