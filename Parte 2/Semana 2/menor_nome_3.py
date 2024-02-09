# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 11:53:15 2024

@author: lfelipe
"""

def menor_nome(nomes):
  """
  Função que recebe uma lista de strings com nomes de pessoas como parâmetro e devolve o nome mais curto (em razão da soma dos valores ASCII das letras de cada nome) presente na lista.

  Argumentos:
    nomes: lista de strings com nomes de pessoas.

  Retorno:
    string com o nome mais curto presente na lista, com a primeira letra maiúscula e seus demais caracteres minúsculos.
  """
  # Normalizando os nomes (removendo espaços em branco e convertendo para letras minúsculas)
  nomes_normalizados = [nome.strip().lower() for nome in nomes]

  # Encontrando o menor comprimento de um nome
  menor_comprimento = min(len(nome) for nome in nomes_normalizados)

  # Encontrando o primeiro nome com o menor comprimento
  menor_nome = None
  for nome in nomes_normalizados:
    if len(nome) == menor_comprimento:
      menor_nome = nome
      break

  # Retornando o menor nome com a primeira letra maiúscula
  return menor_nome[0].upper() + menor_nome[1:]

# Exemplo de uso
# nomes = [" Ana", "João Silva", " Maria", " Pedro", "   Joana  "]
# menor_nome = menor_nome(nomes)
# print(f"O menor nome da lista é: {menor_nome}")
