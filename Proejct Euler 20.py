# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 11:14:31 2015

@author: sya236
"""
def factorial(n):
    new = 1
    final = 0
    for x in range(1, n + 1):
        new = x * new
    while new:           
        digit = new % 10            
        new //= 10
        final += digit
    return (final)

print (factorial(100))