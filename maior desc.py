# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 22:15:21 2019

@author: Daniel Rocha
"""
"""
prim = int(input("Insira o primeiro numero: "))
seg = int(input("Insira o segundo numero: "))
ter = int(input("Insira o terceiro numero: "))

if prim > seg and prim > ter and seg > ter:
    print("Esta é a ordem decrescente: " ,prim ,seg ,ter)
elif prim > seg and prim > ter and ter > seg :
    print("Esta é a ordem decrescente: " ,prim ,ter ,seg)
    
elif seg > prim and seg > ter and ter > prim:
    print("Esta é a ordem decrescente: " ,seg ,ter ,prim)
elif seg > prim and seg > ter and prim > ter:
    print("Esta é a ordem decrescente:",seg ,prim ,ter) 
    
elif ter > seg and ter > prim and seg > prim:
    print("Esta é a ordem decrescente:" ,ter , seg ,prim)
else:
    print("Esta é a ordem decrescente:",ter ,prim ,seg) 
    """
    
numeros = []

for numero in range(1,4):
 numeros.append(int(input("Entre com o %s numero: " %numero)))   
 
numeros.sort()
numeros.reverse()

print("Esta é a ordem descrescente dos numeros: %s" %numeros)
