# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 15:49:28 2024

@author: lfelipe
"""
n = 1

lista = []

while n != 0:
    n = int(input("Digite os valores: "))
    lista.append(n)
lista.reverse()
lista.remove(0)
for i in lista:
    print(i)