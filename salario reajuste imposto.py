# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 06:18:37 2019

@author: Brainiac
"""
"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do 
Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto 
menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% 
Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
No exemplo o valor da hora é 5 e a quantidade de hora é 220. """


bruto = int(input("Qual é o seu salario? "))
fgts = 11
inss = 10
if bruto <= 900:
    ir = 0
elif bruto <= 1500:
 ir = 5
elif bruto <= 2500:
 ir = 10
elif bruto > 2500:
 ir = 20

valor_ir = bruto * ir/100 

valor_fgts = bruto * fgts/100

valor_inss = bruto * inss/100

descontos = valor_ir + valor_inss

liquido = bruto - descontos


print("Valor do imposto de renda: %s" %valor_ir)
print("Valor do fgts depositado pela empresa: %s" %valor_fgts)
print("valor do INSS: %s" %valor_inss)
print("Valor dos descontos: %s" %descontos)
print("Seu salario liquido é: %s" %liquido)
   