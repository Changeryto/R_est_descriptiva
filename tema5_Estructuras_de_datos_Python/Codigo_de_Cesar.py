# -*- coding: utf-8 -*-
"""
Created on Sun May  2 21:13:02 2021

@author: ruben
"""

cesar = {
    "A": "D",
    "B": "E",
    "C": "F",
    "D": "G",
    "E": "H",
    "F": "I",
    "G": "J",
    "H": "K",
    "I": "L",
    "J": "M",
    "K": "N",
    "L": "O",
    "M": "P",
    "N": "Q",
    "O": "R",
    "P": "S",
    "Q": "T",
    "R": "U",
    "S": "V",
    "T": "W",
    "U": "X",
    "V": "Y",
    "W": "Z",
    "X": "A",
    "Y": "B",
    "Z": "C",
    " ": " "
}

f = input("Frase a convertir: ")
fn = ""
for l in f:
    try:
        fn += cesar.get(l.upper())
    except:
        fn += l
    
print("\nNueva frase:\n" + fn)
    
    
    
    
    
    
    
    