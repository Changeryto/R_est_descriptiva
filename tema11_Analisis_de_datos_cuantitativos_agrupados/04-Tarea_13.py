# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 09:38:24 2022

@author: ruben
"""
import pandas as pd
import numpy as np
#Da el algoritmo para reproducir el proceso de generación de clases y 
#sus marcas donde el número de clases ha sido obtenido con la regla de la Scott 
#en Python.

dc = pd.read_table("https://raw.githubusercontent.com/joanby/r-basic/master/data/datacrab.txt",sep=" ")
cw = dc["width"].values
"""
class Scott():
    
    @staticmethod
    def nclass(data):
        As = 3.5 * np.std(data) * (len(data)**(-1/3))
        k = np.ceil((max(data)-min(data))/(As))
        return k
    
    @staticmethod
    def classmarks(data):
        cid = len(str(data[0]).split(".")[1])
        A = (max(data)-min(data)) / Scott.nclass(data)
        A = round(A,cid)
        L1 = min(data) - (1/2 * 0.1)
        L2 = L1 + A
        #L = L1 + A*np.arange(0,Scott.nclass(data)+1)
        #return L
        X1 = (L1 + L2)/2
        X = X1 + A * np.arange(0,Scott.nclass(data))
        return X

n = len(cw)
As = 3.5 * np.std(cw) * n** (-1/3)
k = np.ceil((max(cw)-min(cw)) / As)

A = (max(cw)-min(cw)) / k

A = float(input("A = "+ str(A) +"\n\nA = "))

L1 = min(cw) - (1/2 * 0.1)
L2 = L1 + A

L = L1 + A*np.arange(0,k+1)

X1 = (L1 + L2)/2
X = X1 + A*np.arange(0,k)
"""

class Scott:
    
    @staticmethod
    def nclass(data):
        n = len(data)
        As = 3.5 * np.std(data) * n** (-1/3)
        k = np.ceil((max(data)-min(data)) / As)
        return k
    
    @staticmethod
    def classmarks(data):
        k = Scott.nclass(data)
        A = (max(data)-min(data)) / k
        
        A = float(input("A = "+ str(A) +"\n\nA = "))
        
        L1 = min(data) - (1/2 * 0.1)
        L2 = L1 + A
        
        #L = L1 + A*np.arange(0,k+1)
        
        X1 = (L1 + L2)/2
        X = X1 + A*np.arange(0,k)
        
        return X
        


#Da el algoritmo para reproducir el proceso de generación de clases y 
#sus marcas donde el número de clases ha sido obtenido con la regla de la raíz 
#en Python.

class Sqrt_rule:
    
    @staticmethod
    def nclass(data):
        n = len(data)
        k = np.ceil(np.sqrt(n))
        return k
    
    @staticmethod
    def classmarks(data):
        k = Sqrt_rule.nclass(data)
        A = (max(data)-min(data)) / k
        
        A = float(input("A = "+ str(A) +"\n\nA = "))
        
        L1 = min(data) - (1/2 * 0.1)
        L2 = L1 + A
        
        #L = L1 + A*np.arange(0,k+1)
        
        X1 = (L1 + L2)/2
        X = X1 + A*np.arange(0,k)
        
        return X


#Da el algoritmo para reproducir el proceso de generación de clases y 
#sus marcas donde el número de clases ha sido obtenido con la regla de la 
#Sturges en Python.

class Sturges:
    
    @staticmethod
    def nclass(data):
        n = len(data)
        k = np.ceil(1+np.log2(n))
        return k
    
    @staticmethod
    def classmarks(data):
        k = Sturges.nclass(data)
        A = (max(data)-min(data)) / k
        
        A = float(input("A = "+ str(A) +"\n\nA = "))
        
        L1 = min(data) - (1/2 * 0.1)
        L2 = L1 + A
        
        #L = L1 + A*np.arange(0,k+1)
        
        X1 = (L1 + L2)/2
        X = X1 + A*np.arange(0,k)
        
        return X

#Da el algoritmo para reproducir el proceso de generación de clases y 
#sus marcas donde el número de clases ha sido obtenido con la regla de la  
#Freedman-Diaconis en Python.


class FD:
    
    @staticmethod
    def nclass(data):
        n = len(data)
        Afd = 2 * (np.quantile(cw,0.75) - np.quantile(cw,0.25)) * n**(-1/3)
        k = np.ceil((max(data)-min(data)) / Afd)
        return k
    
    @staticmethod
    def classmarks(data):
        k = FD.nclass(data)
        A = (max(data)-min(data)) / k
        
        A = float(input("A = "+ str(A) +"\n\nA = "))
        
        L1 = min(data) - (1/2 * 0.1)
        L2 = L1 + A
        
        #L = L1 + A*np.arange(0,k+1)
        
        X1 = (L1 + L2)/2
        X = X1 + A*np.arange(0,k)
        
        return X
    
    
    
    
if __name__ == "__main__":
    print(FD.nclass(cw))
    print(FD.classmarks(cw))