# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 01:19:25 2021

@author: ruben
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 256, endpoint = True)

S, C = np.sin(x), np.cos(x)

plt.figure(figsize = (12, 6))
plt.plot(x, S, color="blue", linewidth = "1.2", linestyle = "-", label = "Seno")

plt.plot(x, C, color="green", linewidth = "1.2", linestyle = "-", label = "Coseno")

plt.xlim(x.min()*1.1, x.max()*1.1)
plt.ylim(S.min()*1.1, S.max()*1.1)
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],#Escoger num en el eje
           [r"$-\pi$", r"$-\pi / 2}$","", r"$\pi / 2$", r"$\pi$"]) #Escoger expresión
plt.yticks(np.linspace(-1, 1, 3, endpoint=True),
           ["-1", "", "+1"])

ax = plt.gca() #Acceso a los ejes actuales
ax.spines['right'].set_color("none") #Quita el eje de la izq.
ax.spines["top"].set_color("none")

ax.xaxis.set_ticks_position("bottom")
ax.spines["bottom"].set_position(("data", 0)) #Mueve los datos al eje
ax.yaxis.set_ticks_position("left")
ax.spines["left"].set_position(("data", 0))

plt.legend(loc = "upper left")

x0 = 2*np.pi / 3
plt.plot([x0, x0], [0, np.sin(x0)], color = "blue",
         linewidth = 2.5, linestyle = "--")
plt.scatter([x0,], [np.sin(x0),], 50, color = "blue") #Añade el punto
plt.annotate(r"$\sin(\frac{2 \cdot \pi }{3}) = \frac{\sqrt{3}}{2}$",
             xy = (x0, np.sin(x0)), xycoords = "data",
             xytext = (+20, +40), textcoords = "offset points",
             fontsize = 16, arrowprops = dict(arrowstyle = "->",
                                              connectionstyle = "arc3,rad=.2"))
plt.plot([x0, x0], [0, np.cos(x0)], color = "green",
         linewidth = 2.5, linestyle = "--")
plt.scatter([x0,], [np.cos(x0),], 50, color = "green")
plt.annotate(r"$\cos(\frac{2 \cdot \pi }{3}) = - \frac{1}{2}$",
             xy = (x0, np.cos(x0)), xycoords = "data",
             xytext = (-90, -40), textcoords = "offset points",
             fontsize = 16, arrowprops = dict(arrowstyle = "->",
                                              connectionstyle = "arc3,rad=.2"))

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor = "grey", edgecolor = "None", alpha = 0.6))




plt.show()
