# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 13:50:58 2024

@author: lfelipe
"""
n = 1

lista = []

while n != 0:
    n = int(input("Digite os valores: "))
    lista.append(n)
lista.reverse()

print(lista)