import math

def delta(a,b,c):
    return b ** 2 - 4 * a * c

def main():
    a = float(input("Digite o valor da primeira constante: "))
    b = float(input("Digite o valor da segunda constante: "))
    c = float(input("Digite o valor da terceira constante: "))
    imprime_raizes(a,b,c)

def imprime_raizes(a,b,c):
    d = delta(a,b,c)
    if delta == 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        print("a raiz desta equação é", x1)
    else:
        if d < 0:
            print("esta equação não possui raízes reais.")
        else:
            x1 = (-b + math.sqrt(d)) / (2 * a)
            x2 = (-b - math.sqrt(d)) / (2 * a)
            if x1<x2:
                print("as raízes da equação são", x1, "e", x2)
            else:
                print("as raízes da equação são", x2, "e", x1)