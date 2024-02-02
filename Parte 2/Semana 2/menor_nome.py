# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 16:32:56 2024

@author: lfelipe
"""

# Escrever uma função que recebe uma lista de strings contendo nomes de pessoas
# como parâmetro e devolve o nome mais curto. A função deve ignorar espaços
# antes e depois do nome ('str.strip()') e deve devolver o nome "capitalizado"
# ('str.capitalize()'), i.e., apenas com a 1a letra maiúscula.
# str.capitalize().strip()

def altera_nomes():
    i = 1
    nomes = []
    nome = input("Digite o " + str(i) +"o nome (aperte enter para sair):")
    if not nome:
        return None
    
    while nome:
        nomes.append(nome)
        i += 1
        nome = input("Digite o " + str(i) +"o nome (aperte enter para sair):")
    
    nome_mais_curto = nomes[0].strip().capitalize()
    
    for nome in nomes:
        nome = nome.strip().capitalize()
        if len(nome) < len(nome_mais_curto):
            nome_mais_curto = nome
    return nome_mais_curto
    
    