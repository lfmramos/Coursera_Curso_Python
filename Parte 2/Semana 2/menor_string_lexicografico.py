# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 14:07:50 2024

@author: lfelipe
"""

# Escreva uma função que recebe um array de strings como parâmetro e devolve o primeiro string na ordem lexicográfica, ignorando'se letras maiúsculas e minúsculas.

def menor_string():
    i = 1
    nomes = []
    nome = input("Digite o " + str(i) +"o nome (aperte enter para sair):")
    if not nome:
        return None
    
    while nome:
        nomes.append(nome)
        i += 1
        nome = input("Digite o " + str(i) +"o nome (aperte enter para sair):")
    
    menor_str_lexico = nomes[0].lower()
    
    for nome in nomes:
        nome = nome.lower()
        if ord(nome[0]) < ord(menor_str_lexico[0]):
            menor_str_lexico = nome
    return menor_str_lexico