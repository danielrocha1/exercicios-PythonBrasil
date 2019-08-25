# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 20:57:05 2019

@author: Brainiac
"""

notas = []
nota_soma = 0
media = float
for num in range(1,5):
 notas.append(int(input("Informe a %sª nota: " %num)))
for x in range(0, len(notas)):
  print(" {}ª Nota: {} ".format(x +1 ,notas[x])) 
media = sum(notas) / len(notas)
print(media)
