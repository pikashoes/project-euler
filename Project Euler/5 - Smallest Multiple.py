# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 15:40:51 2016

@author: pikashoes

Question:
What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20?
"""

import math
from functools import reduce

def getNum():
    f = reduce(lambda a,b: lcm(a, b),
               [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                11, 12, 13, 14, 15, 16, 17, 18,
                19, 20])
    return int(f)


def lcm(a, b):
    print((a * b) / math.gcd(int(a), int(b)))
    return (a * b) / math.gcd(int(a), int(b))
             
print(getNum())
