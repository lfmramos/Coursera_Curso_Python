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
        self.perimetro = self.a + self.b + self.c
        return self.perimetro
    
    def retangulo(self):
        if (self.a ** 2) == (self.b ** 2) + (self.c ** 2):
            return True
        if (self.b ** 2) == (self.a ** 2) + (self.c ** 2):
            return True
        if (self.c ** 2) == (self.b ** 2) + (self.a ** 2):
            return True
        else:
            return False