# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 05:25:19 2019

@author: Brainiac
"""

"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo: """

hora = int(input("Quanto voce recebe por hora: "))
mes = int(input("Quantas horas voce trabalha no mes: "))
sal = hora * mes

imp_renda = sal * 11 /100
inss = sal * 8 /100
sind = sal * 5 /100

print("Este é o seu salario bruto: %1.2f Reais" %(sal))
print("Voce pagou: %1.2f Reais ao INSS" %(inss))
print("Voce pagou: %1.2f Reais ao Imposto de Renda" %imp_renda)
print("Voce pagou: %1.2f Reais ao Sindicato" %sind)
sal_liq = sal - imp_renda - inss - sind
desc = imp_renda + inss + sind
print("Seu total de desconto é: %1.2f reais" %(desc))
print("Seu salario liquido é: %1.2f Reais "%(sal_liq))