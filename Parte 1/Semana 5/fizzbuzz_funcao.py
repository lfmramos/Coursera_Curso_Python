# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 13:14:18 2024

@author: lfelipe
"""

def fizzbuzz(x):
    if (x%3 == 0) and (x%5 != 0):
        return "Fizz"
    if (x%3 != 0) and (x%5 == 0):
        return "Buzz"
    if (x%3 == 0) and (x%5 == 0):
        return "FizzBuzz"
    else:
        return x