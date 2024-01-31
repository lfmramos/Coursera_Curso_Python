# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 16:58:33 2024

@author: lfelipe
"""

def n_primos(n):
    """
    Retorna a quantidade de números primos entre 2 e n (incluindo 2 e, se for o caso, n).

    Args:
    - n: número inteiro maior ou igual a 2.

    Returns:
    - count_primos: quantidade de números primos entre 2 e n.
    """
    def eh_primo(numero):
        """
        Verifica se um número é primo.

        Args:
        - numero: número inteiro.

        Returns:
        - True se o número for primo, False caso contrário.
        """
        if numero < 2:
            return False
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                return False
        return True

    count_primos = 0

    for i in range(2, n + 1):
        if eh_primo(i):
            count_primos += 1

    return count_primos

# Exemplo de uso
numero = int(input("Digite um número inteiro maior ou igual a 2: "))
resultado = n_primos(numero)
print(resultado)
