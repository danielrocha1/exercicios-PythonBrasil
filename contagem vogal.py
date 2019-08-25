# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 21:40:18 2019

@author: Brainiac
"""
vogal1 = []
conso = []
letra = []
vogal_cont = 0
conso_cont = 0
vogal = ["a","e","i","o","u"]
for x in range(1,11):
    letra = input("Entre com uma letra:")
    if letra in vogal:
        vogal_cont = vogal_cont + 1
        vogal1.append(letra)
    else :
        conso_cont = conso_cont + 1
        conso.append(letra)
print("Foram estas {} consoantes".format(conso))
print("Foram estas {} vogais".format(vogal1))
print("Foram {} Consoantes".format(conso_cont))
print("Foram {} Vogais".format(vogal_cont))