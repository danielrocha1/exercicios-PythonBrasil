# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 05:47:24 2019

@author: Brainiac
"""

int1 = int(input("Entre com um numero inteiro: "))
int2 = int(input("Entre com mais um numero inteiro: "))
flt = float(input("Entre com um numero real: "))

db = ( int1 * 2) * (int2 / 2.0)
som = int1 * 3
  
print("O dobro do primeiro vezes com a metade do segundo é:" ,db)
print("A soma do triplo do primeiro mais o terceiro numero é: ",som+flt )
print("O terceiro numero elevado ao cubo é: " ,flt**3)