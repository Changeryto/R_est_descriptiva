# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 22:40:07 2021

@author: ruben
"""

'''
Escribe una secuencia de instrucciones 
que permitan leer un número real por pantalla y que muestre si el número es positivo o no.'''

while True:
    try:
        n = float(input("Excribe el número que quieres analzar: "))
        if n < 0:
            print("Tu número " + str(n) + " es negativo")
        elif n > 0:
            print("Tu número " + str(n) + " es postivo")
        elif n == 0:
            print("Tu número es 0")
    except Exception as ex:
        print("No has itroducido un número, vuelve a intentarlo", type(ex))
    else:
        break
    
'''
Escribe una secuencia de instrucciones que permitan leer un número real 
por pantalla y que muestre si el número está en el rango entre -5 y 5'''

while True:
    try:
        n = float(input("Excribe el número que quieres analzar si está entre [5 y -5]: "))
        if n <= 5 and n >= -5:
            print(f'Tu número {n} está entre 5 y -5')
        else:
            print(f'Tu número {n} está fuera de [-5, 5]')
    except Exception as ex:
        print("Se introdujo un valor incorrecto: ", type(ex))
    else:
        break
    
'''
Escribe una secuencia de instrucciones que permitan leer las coordenadas de un punto (x, y)
 e indique en cuál de los cuatro cuadrantes se encuentra dicho punto. '''
 
while True:
     try:
         x = float(input("Introduce la coordenada x =  "))
         y = float(input("Introduce la coordenada y =  "))
         if x > 0 and y > 0:
             print(f'Tus coordenadas x = {x} e y = {y} están en el cuadrante (+, +) o I')
         elif x < 0 and y > 0:
            print(f'Tus coordenadas x = {x} e y = {y} están en el cuadrante (-, +) o II')
         elif x < 0 and y < 0:
            print(f'Tus coordenadas x = {x} e y = {y} están en el cuadrante (-, -) o III')
         elif x > 0 and y < 0:
            print(f'Tus coordenadas x = {x} e y = {y} están en el cuadrante (+, -) o IV')
         elif x == 0 and y == 0:
            print(f'Tus coordenadas x = {x} e y = {y} están en el origen')
         elif x == 0 and y > 0:
            print(f'Tus coordenadas x = {x} e y = {y} están en la parte positiva del eje de ordenadas')
         elif x == 0 and y < 0:
            print(f'Tus coordenadas x = {x} e y = {y} están en la parte negativa del eje de ordenadas')
         elif y == 0 and x > 0:
            print(f'Tus coordenadas x = {x} e y = {y} están en la parte positiva del eje de la abscisa')
         elif y == 0 and x < 0:
            print(f'Tus coordenadas x = {x} e y = {y} están en la parte negativa del eje de la abscisa')
     except Exception as ex:
        print("Tus coordenadas son incorrectas o no existen", type(ex))
     else:
        break
 
'''
Escribe una secuencia de instrucciones que permitan leer dos números enteros y muestre 
el cociente de la división entera y el resto.'''

while True:
    try:
        n = float(input("Introduce tu primer número (dividendo):  "))
        m = float(input("Introduce tu segundo número (divisor):  "))
        cdlde = (n // m)
        resto = (n % m)
        print(f'La división entera de tus números es: {cdlde} , y el resto o remanente es: {resto}')
    except Exception as ex:
        print("Los números no fueron introducidos correctamente", type(ex))
    else:
        break
        
        
'''
Escribe una secuencia de instrucciones que permitan leer un número entero es cuadrado 
perfecto o no (piensa la mejor forma de hacerlo con lo que has aprendido hasta ahora)'''

import math
while True:
    try:
        n = float(input("Introduce el número para saber si es cuadrado perfecto: "))
        if (math.sqrt(n) % 1) == 0:
            print(f'Tu número {n} SÍ es un cuadrado perfecto')
        else:
            print(f'Tu número {n} NO es un cuadrado perfecto')
            
    except Exception as ex:
        print("Introduce un número válido ", type(ex))
    else:
        break
 
'''
Escribe una expresión que permita determinar si un número entero positivo puede 
corresponder a un año bisiesto o no. Se consideran años bisiestos aquellos cuyo 
número es divisible por cuatro excepto los años que son múltiplos de 100, a no ser que 
lo sean de 400 (por ejemplo el año 2000 fue bisiesto pero el 2100 no lo será).'''

while True:
    try:
        n = int(input("Introduce tu año a analizar: "))
        if (n % 4) == 0:
            if (n % 100) == 0:
                if (n % 400) == 0:
                    print(f'Tu año {n} es bisisesto')
                else:
                    print(f'Tu año {n} NO es bisisesto')
            else:
                print(f'Tu año {n} es bisisesto')
        else:
            print(f'Tu año {n} NO es bisisesto')
    except Exception as ex:
        print("Introduce un año correcto", type(ex))
    else:
        break
 
'''
Busca la imagen de un tablero de ajedrez en Google y fíjate en la nomenclatura de las 
casillas. Escribe una expresión lea una letra y un número de teclado correspondiente a 
una casilla de un tablero de ajedrez y nos indique si esta casilla es negra o blanca.'''

while True:
    try:
        l = str.upper(input("Introduce la letra de la casilla: "))
        n = int(input("Introduce el número de la casilla: "))
        if l == "A" or l == "C" or l == "E" or l == "G":
            if n == 8 or n == 6 or n == 4 or n == 2:
                print(f"\nLa casilla {l}{n} es blanca")
            elif n <= 8:
                print(f"\nLa casilla {l}{n} es negra")
        elif l == "B" or l == "D" or l == "F" or l == "H" and n <= 8:
            if n == 8 or n == 6 or n == 4 or n == 2:
                print(f"\nLa casilla {l}{n} es negra")
            else:
                print(f"\nLa casilla {l}{n} es blanca")
        else:
            print(f"\nLa casilla {l}{n} no existe")
    except Exception as ex:
        print("\nIntoduce una casilla real", type(ex))
    else:
        break
    
#También pude haber usardo la función split.()
            
