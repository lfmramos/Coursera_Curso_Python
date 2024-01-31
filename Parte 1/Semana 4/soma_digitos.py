# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 17:51:24 2024

@author: lfeli
"""

n = int(input("Digite um número inteiro: "))

soma = 0

while n != 0:
    soma = soma + (n % 10)
    n = n // 10
print(soma)