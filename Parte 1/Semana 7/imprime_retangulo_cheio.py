# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 14:50:53 2024

@author: lfelipe
"""

largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

# Variável de controle
linha = 1

while linha <= altura:
    # Variável de controle
    coluna = 1
    while coluna <= largura:
        print("#", end="")
        coluna += 1
    print() # Move para a próxima linha após imprimir a largura completa
    linha += 1