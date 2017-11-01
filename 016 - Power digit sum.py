# -*- coding: utf-8 -*-
"""
Solved: 11-01-2017, 15:41

What is the sum of the digits of the number 2^1000?

Answer below. There is probably a faster way to do this.
TODO: Rewrite to faster method.
"""

def answer(n):
    x = 2**n
    strx = str(x)
    answer = 0
    for i in strx:
        answer += int(i)
    return answer

print(answer(1000))

