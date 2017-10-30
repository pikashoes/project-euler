# -*- coding: utf-8 -*-
"""
Solved: 10-30-2017

Question:
Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""
def sum_sq_diff():
    sq_sum = sum(x for x in range(101))**2
    sum_sq = sum(map(lambda x: x**2, [n for n in range(101)]))
    return sq_sum - sum_sq
    
print(sum_sq_diff())