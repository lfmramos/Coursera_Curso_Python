def incomodam(n):
    # Caso base: n não é um inteiro estritamente positivo
    if not isinstance(n, int) or n <= 0:
        return ""
    # Caso recursivo: "incomodam " + chamada recursiva com n-1
    else:
        return "incomodam " + incomodam(n-1)

def elefantes(n):
    if n <= 0:
        return ""
    elif n == 2:
        return "Um elefante incomoda muita gente\n" + str(n) + " elefantes incomodam incomodam muito mais\n"
        # return "Um elefante incomoda muita gente\n"
    else:
        return elefantes(n - 1) + str(n - 1) + " elefantes incomodam muita gente\n" + str(n) + " elefantes " + incomodam(n) + "muito mais\n"
