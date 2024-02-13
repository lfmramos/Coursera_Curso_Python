# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 17:07:27 2024

@author: lfelipe
"""
class Triangulo:
    def __init__(self, lado_a, lado_b, lado_c):
        self.a = lado_a
        self.b = lado_b
        self.c = lado_c
    
    def perimetro(self):
        # perimetro é a soma de todos os lados
        self.perimetro = self.a + self.b + self.c
        return self.perimetro
    
    def tipo_lado(self):
        if self.a == self.b == self.c:
            return 'equilátero'
        if (self.a != self.b) and (self.a != self.c) and (self.b != self.c):
            return 'escaleno'
        else:
            return 'isóceles'