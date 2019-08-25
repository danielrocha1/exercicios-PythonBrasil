# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 05:51:06 2019

@author: Brainiac
"""
salario = float(input("Entre com o seu salario:  "))

if salario <= 280.00 :
 perc = 20   
elif salario <= 700.00:
 perc = 15
elif salario <= 1500.00:
 perc = 10
elif salario > 1500.00:
 perc = 5

novo_salario = salario + salario * perc / 100
valor_aumento = (salario * perc/100)

print("Salario antes do reajuste: %1.2f" %salario)

print("Percentual aplicado no salario: %1.2f%% " %(perc))

print("O valor do aumento no salario: %1.2f " %(valor_aumento))

print("Salario após o reajuste: %1.2f " %(novo_salario))   