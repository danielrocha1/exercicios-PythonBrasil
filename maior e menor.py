# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 22:07:49 2019

@author: Brainiac
"""

prim = int(input("Insira o primeiro numero: "))
seg = int(input("Insira o segundo numero: "))
ter = int(input("Insira o terceiro numero: "))

if prim > seg and prim > ter:
    print("Este é o maior numero: " ,prim)
elif seg > prim and seg > ter:
    print("Este é o maior numero: " ,seg)
else:
    print("Este é o maior numero: " ,ter)    
    
if prim < seg and prim < ter:
    print("Este é o menor numero: " ,prim)
elif seg < prim and seg < ter:
    print("Este é o menor numero: " ,seg)
else:
    print("Este é o menor numero: " ,ter)        
    