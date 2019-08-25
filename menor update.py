# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 23:53:04 2019

@author: Brainiac
"""

numeros = []

for numero in range(1,4):
    numeros.append(float(input("Entre com o %s numero: " %numero)))
    
menor = numeros[0]

for numero in numeros:
    if numero < menor:
        menor = numero
        print("Este é o menor numero: %s" %menor)
    