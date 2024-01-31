# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 18:34:38 2024

@author: lfelipe
"""
lista = [2,4,2,2,3,3,1]

def remove_repetidos(lista):
    lista.sort()
    lista2 = []
    for i in lista:
        if i not in lista2:
            lista2.append(i)
    return lista2

# Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros, verifica se tal lista possui elementos repetidos e os remove. A função deve devolver uma lista correspondente à primeira lista, sem elementos repetidos. A lista devolvida deve estar ordenada.

# Dica: Você pode usar lista.sort() ou sorted(lista). Qual a diferença?

# Exemplo:
# >>>lista = [2, 4, 2, 2, 3, 3, 1]
# >>>remove_repetidos(lista)
# [1, 2, 3, 4]
# >>>remove_repetidos([1, 2, 3, 3, 3, 4])
# [1, 2, 3, 4]