def sao_multiplicaveis(m1, m2):
    # Verifica se as matrizes têm as mesmas dimensões
    if len(m1[0]) == len(m2):
    #if len(m1) == len(m2) or len(m1[0]) == len(m2[0]):
        return True
    else:
        return False