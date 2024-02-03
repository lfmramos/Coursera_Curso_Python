# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 14:30:14 2024

@author: lfelipe
"""

def fazAlgo(string):
    pos = 0
    string1 = ""
    string = string.lower()
    stringMa = string.upper()
    while pos < len(string):
        if pos % 2 == 0:
            string1 = string1 + stringMa[pos]
        else:
            string1 = string1 + string[pos]
        pos = pos + 1
    return string1    

print(fazAlgo("paralelepipedo"))