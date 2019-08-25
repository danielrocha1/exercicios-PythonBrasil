# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 22:45:40 2019

@author: Brainiac
"""
def sex(): 
 sexo = input("Digite M se for do sexo masculino ou F se for do sexo feminino :")

 if sexo.upper() == 'M':
  print("voce é do sexo Masculino" )
 elif sexo.upper() == 'F': 
  print("Voce é do sexo Feminino ") 
 else :
  print(" Sexo Inválido ")      

sex()