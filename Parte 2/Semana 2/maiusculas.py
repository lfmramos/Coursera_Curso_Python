def maiusculas(frase):
    # Variável que recebe as letras maiúsculas encontradas:
    letras_maiusculas = ''
    # Iterando sobre cada letra da frase:
    for letra in frase:
        if letra.isupper():
            letras_maiusculas += letra
    return letras_maiusculas