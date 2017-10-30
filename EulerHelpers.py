# -*- coding: utf-8 -*-
"""
Helper Functions to be used
"""
import math

"""
Counts the number of divisors of a number in O(n) time.
TODO: Improve run time.
"""
def count_divisors(num):
    count = 0
    if (num == 1):
        return count + 1
    else:
        for i in range(1, math.floor(math.sqrt(num))+1):
            if (num % i == 0):
                count += 2
    return count


"""
Returns the n'th fibonacci number iteratively.
"""
def get_nth_fibonacci(n):
    count = 0
    f0 = 0
    f1 = 1
    while (count < n):
        temp = f0        
        f0 = f1
        f1 += temp
        count += 1
    return temp
    
#print(get_nth_fibonacci(16))
    #Should be 610