# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 11:23:38 2021

@author: ruben
"""

# fill_between

import matplotlib.pyplot as plt
import numpy as np

n = 256

X = np.linspace(-np.pi, np.pi, n, endpoint=True)



Y = np.sin(2 * X) 


plt.figure(num = 1,figsize = [20, 12])

plt.subplot(2, 1, 1)
plt.plot(X, Y, color='blue', alpha=1.00)
plt.fill_between(X, Y, color="mediumslateblue")

plt.xticks([])
plt.yticks([])

ax = plt.gca()
ax.spines["top"].set_color("none")
ax.spines["left"].set_color("none")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_color("none")

plt.subplot(2, 1, 2)
plt.plot(X, Y, color='blue', alpha=1.00)


plt.fill_between(X, Y, color="mediumslateblue")




Xn = np.append(X[(X >= -np.pi/2) & (X <= 0)] , X[(X >= np.pi/2) & (X <= np.pi)])
Yn = Y[(Y >=-1) & (Y<0)]
plt.fill_between(Xn[range(0, 64)], Yn[range(0, 64)], color = "lightpink")
plt.fill_between(Xn[range(64, 128)], Yn[range(64, 128)], color = "lightpink")


plt.xticks([])
plt.yticks([])

ax = plt.gca()
ax.spines["top"].set_color("none")
ax.spines["left"].set_color("none")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_color("none")


plt.show()

###############################################################################



plt.figure(num = 2,figsize = [5, 3], dpi = 300)
n = 1024

X = np.random.normal(0,1,n)

Y = np.random.normal(0,1,n) 

ang = np.arctan2(X, Y) 


colors = (ang)


plt.scatter(X,Y, c=colors, edgecolors = "black",alpha = 0.6, cmap = "hsv")
plt.xlim(-1, 1)
plt.ylim(-1, 1)


plt.xticks([])
plt.yticks([])

plt.show()


###############################################################################

plt.figure(num = 3,figsize = [5, 3], dpi = 300)

n = 12

X = np.arange(n)

Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n) 

plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')

plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white') 

for x, y in zip(X, Y1):     

        plt.text(x , y + 0.05, '%.1f' % y, ha='center', va='bottom')
        
for x, y in zip(X, Y2):             
        plt.text(x , -y - 0.18, '%.1f' % y, ha='center', va='bottom')
        

plt.ylim(-1.25, +1.25)

plt.show()

###############################################################################


import matplotlib.cm as cm

plt.figure(num = 4, dpi = 300)

Z = np.random.uniform(0, 1, 20)
z = sorted(Z, reverse=True)
colors = cm.binary(z)
explode = np.repeat(0.08, 19)
explode = np.append(explode, 0.2)

plt.pie(x = Z, colors = colors, explode = explode, 
        wedgeprops={"edgecolor":"k",'linewidth': 1, 'linestyle': 'solid', 'antialiased': True})


plt.show()
 








