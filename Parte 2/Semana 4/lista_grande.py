import random

def lista_grande(n):
    return [random.randint(0, 100) for _ in range(n)]

# Nesta implementação, usamos a função randint() do módulo random para gerar
# números inteiros aleatórios entre 0 e 100.
# O comprimento da lista é determinado pelo parâmetro n.
# O laço de compreensão de lista cria uma lista de n números inteiros
# aleatórios e a retorna.