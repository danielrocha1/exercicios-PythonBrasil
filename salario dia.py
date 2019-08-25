# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 05:25:19 2019

@author: Brainiac
"""

mes = int(input("Quanto vocce recebe no mes: "))
dia = int(input("Quantos dias do mes voce trabalha: "))
dia1 = mes / dia
hora = int(input("Quantas horas voce trabalha no dia: "))
hora1= dia1 / hora
print("O valor de suas horas diarias são: ",hora1)