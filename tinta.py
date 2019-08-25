# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 06:36:24 2019

@author: Brainiac
"""

""" Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser 
pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas 
de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço 
total. """

m = int(input("Quantos metros quadrado a area a ser pintada: "))
lt = m / 3
lata = int
lata = lt / 18

if lt % 18 != 0:
 lata += 1
  
print("Voce deverá comprar %1.0f latas " %(lata))
print("Voce irá gastar: %1.2f reais" %(lata * 80))
