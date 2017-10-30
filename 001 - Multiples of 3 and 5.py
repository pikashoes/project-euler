# -*- coding: utf-8 -*-
"""
Solved: 09-10-2015

Re-solving Problem 1 (already solved several years ago
but don't have the solution written anywhere)
"""

def get_mult_three_five(n):
    result = 0
    for num in range(n):
        if (num % 3 == 0) or (num % 5 == 0):
            result += num
    return result
    
print(get_mult_three_five(1000))