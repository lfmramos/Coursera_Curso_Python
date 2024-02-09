# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 14:20:16 2024

@author: lfelipe
"""

import matriz

def soma_matrizes(A, B):
    num_linhas = len(A)
    num_colunas = len(A[0])
    C = matriz.cria_matriz(num_linhas, num_colunas, 0)
    
    for linha in range(num_linhas):# Percorre as linhas da matriz
        for coluna in range(num_colunas): # Percorre as colunas da matriz
            C[linha][coluna] = A[linha][coluna] + B[linha][coluna]
    return C

if __name__ == '__main__':
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    B = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
    print(soma_matrizes(A, B))