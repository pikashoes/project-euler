# -*- coding: utf-8 -*-
"""
Solved: 10-31-2017, 14:44

https://projecteuler.net/problem=7
What is the 10,001st prime number?
"""
import EulerHelpers

def get_answer(n):
    return EulerHelpers.get_nth_prime(n)

print(get_answer(10001))