# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 17:07:27 2024

@author: lfelipe
"""

# Defina a classe Triangulo cujo construtor recebe 3 valores inteiros correspondentes aos lados a, b e c de um triângulo.
# A classe triângulo também deve possuir um método perimetro, que não recebe parâmetros e devolve um valor inteiro correspondente ao perímetro do triângulo.

# t = Triangulo(1, 1, 1)
# # deve atribuir uma referência para um triângulo de lados 1, 1 e 1 à variável t 

# Um objeto desta classe deve responder às seguintes chamadas:
# t.a
# # deve devolver o valor do lado a do triângulo
# t.b
# # deve devolver o valor do lado b do triângulo
# t.c
# # deve devolver o valor do lado c do triângulo

# t.perimetro()
# # deve devolver um inteiro correspondente ao valor do perímetro do triângulo.
  
class Triangulo:
    def __init__(self, lado_a, lado_b, lado_c):
        self.a = lado_a
        self.b = lado_b
        self.c = lado_c
    
    def perimetro(self):
        # perimetro é a soma de todos os lados
        return self.a + self.b + self.c
    
    def retangulo(self):
        if (self.a ** 2) == (self.b ** 2) + (self.c ** 2):
            return True
        if (self.b ** 2) == (self.a ** 2) + (self.c ** 2):
            return True
        if (self.c ** 2) == (self.b ** 2) + (self.a ** 2):
            return True
        else:
            return False

# Ainda na classe Triangulo, escreva um método semelhantes(triangulo) que recebe um objeto do tipo Triangulo como parâmetro e verifica se o triângulo atual é semelhante ao triângulo passado como parâmetro. Caso positivo, o método deve devolver True. Caso negativo, deve devolver False

# Um triângulo é semelhante a outro triângulo se a razão (divisão) entre os comprimentos dos seus lados forem iguais.

# Dica: você pode colocar os lados de cada um dos triângulos em uma lista diferente e ordená-las.

# Exemplo:
# t1 = Triangulo(2, 3, 5)
# t2 = Triangulo(4, 6, 10)
# t1.semelhantes(t2)
# # deve devolver True
    def semelhantes(self, triangulo2):
        lista1 = [self.a, self.b, self.c]
        lista2 = [triangulo2.a, triangulo2.b, triangulo2.c]
        lista1.sort()
        lista2.sort()
        if lista1[0] / lista2[0] == lista1[1] / lista2[1] == lista1[2] / lista2[2]:
            return True
        else:
            return False