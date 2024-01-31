# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 13:21:31 2024

@author: lfelipe
"""

def maximo(x,y,z):
    if x >= y and x >= z:
        return x
    if y >x and y > z:
        return y
    if z > x and z > y:
        return z
    