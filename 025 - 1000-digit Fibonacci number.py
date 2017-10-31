# -*- coding: utf-8 -*-
"""
Solved: 10-31-2017, 14:54

What is the *index* of the first term in the
Fibonacci sequence to contain 1000 digits?
"""

def get_n_digit_fib(n):
    count = 0
    index = 0
    f0 = 0
    f1 = 1
    while (count < n):
        temp = f0        
        f0 = f1
        f1 += temp
        count = len(str(temp))
        index += 1
    return index - 1

print(get_n_digit_fib(1000))