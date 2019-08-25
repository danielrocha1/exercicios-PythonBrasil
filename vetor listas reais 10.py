# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 20:57:05 2019

@author: Brainiac
"""

vec = []

for num in range(1,10):
 vec.append(float(input("Informe o %s numero:" %num)))
vec.sort()
vec.reverse()
print(vec) 