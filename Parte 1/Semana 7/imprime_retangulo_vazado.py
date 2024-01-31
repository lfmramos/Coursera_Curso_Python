# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 16:53:19 2024

@author: lfelipe
"""

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
        if linha == 1 or linha == altura or coluna == 1 or coluna == largura:
            print('#', end='')
        else:
            print(' ', end='')
        coluna += 1
    print() # Move para a próxima linha após imprimir a largura completa
    linha += 1