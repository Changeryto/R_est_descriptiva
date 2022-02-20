# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 15:28:56 2021

@author: ruben
"""

import pandas as pd
import numpy as np


""" Importar DF en Python """

df = pd.read_csv("C:\\Programación ExL\\R_y_Python\\tema7_Data_frames\\Data_frames_Python\\wine.data", sep=",", decimal=".",names=("Class Distribution","Alcohol", "Malic acid", "Ash", "Alcalinity of ash", "Magnesium", "Total phenols", "Flavanoid", "Nonflavanoid phenols", "Proanthocyanins", "Color intensity", "Hue", "OD280/OD315 of diluted wines", "Proline"))

# sep = "separadpr"
# decimal = "separador decimal"
# encoding = "UTF-8"
# index_col = 
# header = 

""" Imprimir datos extremos"""

print(df.head(8))

print(df.tail(8))

"""Acceder a las posiciones de un DF"""

# Para un dato, identificadores de naturales

### Regresa un diccionario con la primer fila de valores

df.loc[0]


### Regresa un sub DF con la primer fila y todas las colúmnas

df.loc[[1]]

df.loc[0] == df.iloc[0] # Esto regresa Trues

###  Para regresar un sub Data Frame

df[12:20] # Fila 12 a la 19

df[10:95:5] # Fila 10 a la 95 de 5 en 5

### Acceder a columnas

df.Alcohol #df.colname

"""Funciones de columnas """

df.Alcohol.mean()

df.Alcohol.median()

df.Alcohol.var()

df.Alcohol.describe()

# Para funcionar con todo el DF

df.describe()

""" Trasponer una tabla de datos """

df.describe().transpose()

""" Encontrar tamaño"""
df.shape


"""Cargar DF de internet"""

# df2 = pd.read_table("URL")










"""Crear un DF"""

# pd.DataFrame(diccionario)

df3 = pd.DataFrame({
    "A": np.random.rand(10),
    "B": np.random.rand(10),
    "C": np.random.rand(10)
    })

df3.describe()

#Hacer la media para cada una de las colúmnas
df3.mean(axis="columns")



df4 = pd.DataFrame({
    "keys": ("A", "B", "C"),
    "values": range(3)
    })

"""Agrupar y operar todos los que son de un mismo factor"""

df4.groupby("keys").mean()









"""Agregados de DF"""

df5 = pd.DataFrame({
    "key": ("A", "B", "C", "A", "B", "C"),
    "value1" : range(6),
    "value2": np.random.randint(0, 100, 6)
    })

# aggregate puede tomar str, funcion o lista de operaciones


df5.groupby("key").aggregate(["min", np.median, np.mean, max]) #.aggregate(vector de operaciones)

#Indicar con un diccionario

df5.groupby("key").aggregate({
    "value1": "min",
    "value2": "max"
    })




"""Filter"""

df5.groupby("key").std()

# Se crea una función que regresa las DS menores  a 1
def filter_func(x):
    return x("value2").std() < 1

df5.groupby("key").filter(filter_func)


"""Transform"""

df5.groupby("key").transform(lambda x : x-x.mean()) #Centralié los datos






"""Apply"""

def normalizar_col2(x):
    x["value1"] /= x["value2"].sum()
    return x

df5.groupby('key').apply(normalizar_col2)









"""Parámetros de función groupby"""

L = [0, 1, 0, 1, 2, 0]
print(df)
df5.groupby(L).sum() # L son ides

df.groupby("Alcohol").sum() # Se usó una colname






"""set_index"""
# Para dar nombre a las filas

df5_2 = df5.set_index("key")
# Y ahora los índices son ABCABC





"""mapping"""

mapping = {
    "A": "vocal",
    "B": "consonante",
    "C": "consonante"}

df5_2.groupby(mapping).sum()
# Al haber metido un diccionario, reordena los factores del índice


### Si queremos cambiar los factores a minúscula

df5_2.groupby(str.lower).mean()




"""Exportación de gráficos de Data Frames"""

years = [year for year in range(1900, 2020)]
deads = [(y + np.random.uniform(0, 100) - 1850) for y in years]

df6 = pd.DataFrame({
    "year": years,
    "deads": deads
    })

df6.head()

ploteo = df6.plot(x = "year", y = "deads", figsize =(10, 8))

figura = ploteo.get_figure()
figura.savefig("ploteo.png")






















