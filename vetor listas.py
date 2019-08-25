# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 20:57:05 2019

@author: Brainiac
"""

vec = []

for num in range(1,5):
 vec.append(int(input("Informe o %s numero:" %num)))
vec.sort()

print(vec) 