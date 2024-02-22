def soma_lista(lista):
    # Caso base: se a lista estiver vazia, a soma é zero
    if not lista:
        return 0
    # Caso recursivo: soma o primeiro elemento com a soma do restante da lista
    else:
        return lista[0] + soma_lista(lista[1:])