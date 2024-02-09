def conta_letras(frase, contar="vogais"):
    """
    Conta o número de vogais ou consoantes presentes em uma frase.

    Args:
    - frase: uma string contendo uma frase.
    - contar: uma string indicando se devemos contar vogais ou consoantes.
              Pode ser "vogais" ou "consoantes". O valor padrão é "vogais".

    Returns:
    - numero_letras: número de vogais ou consoantes, dependendo do valor do parâmetro contar.
    """
    # Define as letras a serem contadas
    if contar == "vogais":
        letras = "aeiouAEIOU"
    elif contar == "consoantes":
        letras = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    else:
        return "Valor inválido para o parâmetro contar. Use 'vogais' ou 'consoantes'."

    # Conta as letras na frase
    numero_letras = 0
    for letra in frase:
        if letra in letras:
            numero_letras += 1

    return numero_letras