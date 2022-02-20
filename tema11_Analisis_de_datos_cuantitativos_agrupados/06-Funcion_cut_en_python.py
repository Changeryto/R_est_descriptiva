# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 12:38:37 2022

@author: ruben
"""

import numpy as np
import pandas as pd
import seaborn as sb

# Tablas de pivotaje

titanic = sb.load_dataset("titanic")
print("\n\n\n",titanic.head()) #Parte del DF del Titanic

print("\n\n\n",titanic.groupby("sex").mean()) #Media de todas las características por sexo

print("\n\n\n",titanic.groupby("sex")[["survived"]].mean()) #Media de supervivencia según sexo


print("\n\n\n",titanic.groupby(["sex", "pclass"])["survived"].aggregate("mean").unstack()) #Media de supervivencia según sexo vs clase.


## Para no hacer comandos tan complejos

print("\n\n\n",titanic.pivot_table("survived", index="sex", columns="pclass")) #Media de supervivencia (a) según sexo(index) vs clase (columns).

# Función cut
## breaks es cambiado por bins
age = pd.cut(titanic["age"], bins = [0,18,25,35,50,65,100],
             right=False,
             include_lowest=True)

print("\n\n\n",age)

## nueva tabla de pivotaje

print(titanic.pivot_table("survived", index = ["sex", age], columns ="class"))


# Función qcut de pandas agrupa los datos en los cuartiles

fare = pd.qcut(titanic["fare"], q=4, 
               labels=["Q1","Q2","Q3","Q4"])
print("\n\n\n",fare)

print("\n\n\n",titanic.pivot_table("survived", index=["sex",age], columns=[fare, "pclass"])) #Compara sexo, edad, clase (1 a 3) y cuantil del precio del boleto (Q4 es máximo).

### DataFrame.pivot_table(data, values=None(Principal), index=Filas, columns=columnas, aggfunc="mean por defecto", fill_value=None(rellenar NA), margins=False(True hace el total por filas y por columnas), dropna = True(descarta NAs), margins_name = "All"(nombres que aparecen en caso de calcular las marginales, todos por defecto))

## A la función de agregación puedes agregar un diccionario

print("\n\n\n", titanic.pivot_table(index = "sex",
                    columns="class",
                    aggfunc = {"survived":sum, "fare": "mean"}))


print("\n\n\n",titanic.pivot_table("survived",
                    index="sex",
                    columns="class",
                    margins=True,
                    margins_name="Total"))






