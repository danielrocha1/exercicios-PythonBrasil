# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 06:01:02 2019

@author: Daniel Rocha
"""
""" Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7 """

h = float(input("Qual é a sua altura: "))
sex = input(("Sendo H para homem e M para mulher, qual o seu Genero: ")).upper()
if sex == 'H':
 calc = 72.7 * h - 58
elif sex == 'M':
 calc = 62.1* h - 44.7

print("Este é o seu peso ideal: %1.2f " %(calc))
