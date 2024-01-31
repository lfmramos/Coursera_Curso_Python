# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 11:43:55 2024

@author: lfelipe
"""
letras = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

def vogal(x):
    if x in letras:
        return True
    else:
        return False
    
    # if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
    #     return True
    # else:
    #     return False