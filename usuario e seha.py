# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 23:17:39 2019

@author: Brainiac
"""

user = input("Entre com o nome de usuario: ")
senha = input("Entre com a senha: ")

if user == senha:
 while user == senha:
    print("usuario e senha não podem ser o mesmo. ")
    user = input("Entre com o nome de usuario: ")
    senha = input("Entre com a senha: ")
    print("usuario e senha não podem ser o mesmo. ")