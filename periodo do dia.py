# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 05:19:25 2019

@author: Brainiac
"""
print("M para Matutino, T para a Tarde e N para a Noite")
turno = input("Em qual turno você estuda: ").upper()

if turno == "M" :
 print("Bom dia!")
 
elif turno == "T":
 print("Boa tarde!")

elif turno == "N":
 print("Boa noite!")

else:
    print("Valor Inválido!")