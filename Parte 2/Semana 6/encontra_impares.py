def encontra_impares(lista):
    # Caso base: lista vazia
    if not lista:
        return []
    # Caso recursivo: verifica se o primeiro elemento é ímpar e chama a função recursivamente com o restante da lista
    else:
        impares = []
        if lista[0] % 2 != 0:
            impares.append(lista[0])
        impares.extend(encontra_impares(lista[1:]))
        return impares