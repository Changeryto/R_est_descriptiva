# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 23:54:43 2021

@author: ruben
"""

import matplotlib.pyplot as plt

import numpy as np

from matplotlib.ticker import NullFormatter

mu = 0.5
sd = 0.3
y = mu + sd*np.random.randn(1000) 

y = y[(y >= 0) & (y < 1)]
y.sort()
x = np.arange(len(y))




plt.figure(figsize = (10, 8))

plt.subplot(2, 2, 1)
plt.plot(x, y)
plt.yscale("linear")
plt.xscale("linear")
plt.title("Escala lineal")
plt.grid(True)

plt.subplot(2, 2, 2)
plt.plot(x, y)
plt.yscale("log")
plt.title("Escala semilogarítmica")
plt.grid(True)

plt.subplot(2, 2, 3)
plt.plot(x, y - y.mean())
plt.yscale("symlog", linthreshy=0.01)
plt.title("Escala Log simétrico")
plt.grid(True)

plt.subplot(2, 2, 4)
plt.plot(x, y)
plt.yscale("logit")
plt.title("Escala logística")
plt.gca().yaxis.set_minor_formatter(NullFormatter())
plt.grid(True)

plt.subplots_adjust(top = 0.92, bottom = 0.08, left = 0.1, right = 0.95, hspace = 0.35, wspace = 0.35)



plt.show()


