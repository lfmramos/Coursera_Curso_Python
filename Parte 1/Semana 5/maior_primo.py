# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 18:40:03 2024

@author: lfelipe
"""
def maior_primo(x):
   while x != 0:
       resultado = primo(x)
       if (resultado == True):
           return x
       else:
           x = x - 1
        
def primo(x):
    primo = True
    for k in range(2,x):
        if (x % k == 0):
            primo = False
    return primo