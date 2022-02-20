# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 01:35:30 2021

@author: ruben
"""
while True:
    try:
        user = int(input("Número hasta el que quiere cribar: "))
    except Exception as ex:
        print("Por favor introduce un número entero ewe", type(ex))
    else:
        break
    
    
con = 3
numeros = [2]
while con != user:
    numeros.append(con)
    con += 1
    
for n in numeros:
    print("Primo:", n)
    for m in range(2, user):
        try:
            numeros.remove(n * m)
        except:
            continue