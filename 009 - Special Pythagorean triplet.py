"""
Solved: 01-09-2018, 12:01
https://projecteuler.net/problem=9
"""

import time

def get_return(r):
    #Get r^2
    #Find s, t such that s*t = r^2/2. (Factor pairs)
    #x = r + s, y = r + t, z = r + s + t (Dickson's method)
    #We are looking for something such that x + y + z = 1000, so check this
        #This is 3r + 2s + 2t, so we can check this directly.
    #If x + y + z == 1000, then return x * y * z.
    
    square = r**2
    factor_pairs = get_factor_pairs(square/2)
    for i in factor_pairs:
        s = i[0]
        t = i[1]
        x = r + s
        y = r + t
        z = r + s + t
        if x + y + z == 1000:
            return (x * y * z)

def get_factor_pairs(num):
    answer = []
    if (num == 1):
        return [[1, 1]]
    else:
        for i in range(1, num + 1):
            if (num % i) == 0:
                answer.append([i, num/i])
    return answer

def get_answer():
    start = time.clock()
    
    for i in range(1, 1000):
        x = get_return(i)
        if x is not None:
            elapsed = time.clock() - start
            print("time elapsed: " + str(elapsed))
            print("--------")
            return x

print(get_answer())
