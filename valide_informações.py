# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 02:10:29 2019

@author: Brainiac
"""

comp_nome = True
nome = input("Qual é o seu nome? ")
while comp_nome == True:
    if len(nome) <= 3:
        print("Ação inválida, Nome precisa ter mais que 3 caracteres.")
        nome = input("Qual é o seu nome? ")
    else:
        comp_nome = False

comp_idade = True        
idade = int(input("Quantos anos voce tem? ")) 
while comp_idade == True:
 if idade <= 0:
    print("Ação inválida, Idade precisa ser maior que 0 e menor que 150.") 
    idade = int(input("Quantos anos voce tem? "))
 elif idade > 150:
    print("Ação inválida, Idade precisa ser maior que 0 e menor que 150.") 
    idade = int(input("Quantos anos voce tem? "))
 else:
     comp_idade = False

comp_sal = True

sal = int(input("Qual é o seu salário? ")) 

while comp_sal == True:
 if sal <= 0:
     print("Ação inválida, Salário tem que ser maior que 0")
     sal = int(input("Qual é o seu salário? "))
 else:
     comp_sal = False
comp_sex = True
sex = input("M para masculino e F para Femnino: ").upper()
while comp_sex == True:
    if sex == "F":
        comp_sex = False
        
    elif sex == "M":
        comp_sex = False
    else:
        print("Ação inválida, a letra precisa ser F ou M")
        sex = input("M para masculino e F para Feminino: ").upper()
civil = ("S" , "C" , "V" , "D") 
comp_civil = True
estado = input("S para solteiro, C para casado, V para Viúvo e D para Divorciado. Qual é o seu Estado Civil? ").upper()
while comp_civil == True:
 if estado in civil:
   comp_civil = False
 else:
  print("Ação Inválida.")
  estado = input("S para solteiro, C para casado, V para Viúvo e D para Divorciado. Qual é o seu Estado Civil? ").upper()

print("Seu nome é: %s" %nome)
print("Voce tem: %s anos "%idade)
if sex == "M":
    print("Voce é do sexo Masculino.")
else:
    print("Voce é do sexo Feminino.")
print("Voce é %s" %estado)    
print("Seu salário é de: %s"%sal)