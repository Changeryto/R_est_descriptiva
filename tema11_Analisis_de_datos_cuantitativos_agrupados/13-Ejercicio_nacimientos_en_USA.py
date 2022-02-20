# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 03:11:23 2022

@author: ruben
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

births = pd.read_csv("https://raw.githubusercontent.com/Changeryto/r-basic/master/data/us-births.csv")

print(births.shape, "\n")

print(births.head, "\n")

pivotaje = births.pivot_table("births", index = "year", columns="gender", aggfunc="sum")
print(pivotaje, "\n")

## Visualización por década

births["decade"] = ((births["year"]//10)*10)

print(births.head(), "\n")

print(births.pivot_table("births", index="decade", columns="gender", aggfunc="sum"), "\n")


import seaborn as sb

#%matplotlib inline

sb.set()
plt.figure(figsize = (10,8))
births.pivot_table("births", index="year", columns="gender", aggfunc="sum").plot()

plt.show()

## Herramientas de Pandas

quartiles = np.percentile(births["births"], [25,50,75])

print(quartiles, "\n")

med = quartiles[1] #@med
IQR = quartiles[2] - quartiles[0]
sig = 0.75*IQR


births = births.query("(births > @med - 5*@sig) & (births < @med + 5*@sig)")

births["day"] = births["day"].astype(int)

print(births.shape, "\n")


## Crear objeto Date Time

births.index = pd.to_datetime(10000*births.year + 100*births.month + births.day, format="%Y%m%d")

births["dayofweek"] = births.index.dayofweek

births.pivot_table("births", index="dayofweek", columns="decade", aggfunc="mean").plot()
plt.gca().set_xticklabels(("","Lun", "Mar", "Mie","Jue","Vie","Sab","Dom"))
plt.ylabel("Media de naciemientos por día")
plt.show()


## Nacimientos por fecha

births_by_day = births.pivot_table("births", index=(births.index.month, births.index.day), aggfunc="mean")

births_by_day.index = [pd.datetime(2020, month, day) 
                       for (month, day) in births_by_day.index]

plt.figure(figsize=(12,4))

births_by_day.plot()
plt.show()

















