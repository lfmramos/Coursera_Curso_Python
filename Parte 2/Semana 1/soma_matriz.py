def soma_matrizes(m1, m2):
    """
    Soma duas matrizes.

    Args:
    - m1: matriz representada como uma lista de listas.
    - m2: matriz representada como uma lista de listas.

    Returns:
    - matriz_soma: matriz resultante da soma se as matrizes tiverem dimensões iguais,
                   False caso contrário.
    """
    # Verifica se as matrizes têm as mesmas dimensões
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        return False

    # Inicializa a matriz resultado com zeros
    matriz_soma = [[0 for _ in range(len(m1[0]))] for _ in range(len(m1))]

    # Realiza a soma elemento por elemento
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            matriz_soma[i][j] = m1[i][j] + m2[i][j]

    return matriz_soma