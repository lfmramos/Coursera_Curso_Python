# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 14:27:11 2024

@author: lfelipe
"""

def fazAlgo(string):
    pos = len(string)-1
    string = string.upper()
    while pos >= 0:
        print(string[pos],end = "")
        pos = pos - 1

fazAlgo("paralelepipedo")