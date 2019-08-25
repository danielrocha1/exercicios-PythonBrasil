# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 06:13:02 2019

@author: Brainiac
"""

"""Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de 
São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João
deverá pagar. Imprima os dados do programa com as mensagens adequadas."""


peso = int(input("Quanto KG rendeu a pescada: "))
excesso = peso - 50
multa = excesso * 4

print("A pescada teve: %1.2f Kg em excesso" %(excesso)) 
print("Voce deve: %s reais em multa" %(multa))