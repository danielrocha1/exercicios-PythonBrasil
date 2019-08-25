# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 23:05:16 2019

@author: Brainiac
"""
x = int(input("Entre com um numero de 0 a 10: " ))

while x > 10 or x < 0:
  print("Valor inválido")
  x = int(input("Entre com um numero de 0 a 10: " ))

print("Sua nota é: ",x)        
        
        