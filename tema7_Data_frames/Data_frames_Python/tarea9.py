# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 00:12:37 2021

@author: ruben
"""

import pandas as pd
import numpy as np

run = pd.read_csv("C:\\Programación ExL\\R_y_Python\\tema7_Data_frames\\Data_frames_Python\\run.csv")


# Indica cuantos estudiantes formaron parte del estudio de deporte

print(run.describe())


# Indica cuantos individuos son hombres y cuantos son mujeres


print(run.groupby("genero").aggregate([len]))


# Calcula el porcentaje medio de variación 
# del pulso por minuto entre antes y después de 
# hacer ejercicio 


def cv (x):
    return (np.std(x) / np.mean(x)) * 100

print("El porcentaje medio de variación antes del ejercicio es:", cv(run.pulso_antes),
      "\nEl porcentaje medio de variación después del ejercicio es:", cv(run.pulso_despues),
      "\nLa diferencia es de:", abs(cv(run.pulso_antes) - cv(run.pulso_despues)))

#y compara el valor de los que hacen ejercicio habitualmente y los que no. 
# ¿Observas mucha diferencia?

print(run.groupby("hace_deporte").aggregate([cv]))


#Calcula el porcentaje medio de variación del pulso por minuto entre antes y 
#después de hacer ejercicio  para los estudiantes que hacen ejercicio 
#habitualmente y compara el valor de los hombres con el de las mujeres. ¿Observas mucha diferencia?

hombres = run[run["genero"] == "H"]
mujeres = run[run["genero"] == "M"]

print("CV de hombres:\n", hombres.groupby("hace_deporte").aggregate([cv]))
print("CV de mujeres:\n", mujeres.groupby("hace_deporte").aggregate([cv]))
    
#Calcula el porcentaje medio de variación del pulso por minuto entre antes y 
#después de hacer ejercicio para los estudiantes que no hacen ejercicio 
#habitualmente y compara el valor de los fumadores con los no fumadores. 
#¿Observas mucha diferencia?





#Calcula el porcentaje medio de variación del pulso por minuto entre antes y 
#después de hacer ejercicio de todos los estudiantes según el tipo de actividad
# física que realizan. ¿Observas alguna diferencia?











