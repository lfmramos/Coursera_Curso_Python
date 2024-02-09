def primeiro_lex(lista):
    """
    Retorna o primeiro string na ordem lexicográfica de uma lista de strings.

    Args:
    - lista: uma lista de strings.

    Returns:
    - primeiro: o primeiro string na ordem lexicográfica.
    """
    primeiro = min(lista, key=str.lower)
    return primeiro