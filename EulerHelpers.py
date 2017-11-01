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
Returns a list of all the divisors (including n).
"""
def get_divisors(num):
    answer = []
    if (num == 1):
        return [1]
    else:
        for i in range(1, num + 1):
            if (num % i) == 0:
                answer.append(i)
    return answer

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

"""
Returns the n'th prime number
"""
def get_nth_prime(n):
    if n == 1:
        return 2
    count = 1 #Already counted '2' as being first prime
    num = 3
    while count != n:
        if is_prime(num):
#            print(num)
            count += 1
        num += 2 #can skip the even numbers
    return num - 2
            

"""
Checks if the number is prime
"""
def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    
    root = math.floor(math.sqrt(n))
    for i in range(3, root + 1, 2): #only check odd not even
        if n % i == 0:
            return False
    return True

#print(is_prime(5))
#print(is_prime(13))
#print(is_prime(42))
#print(get_nth_prime(100))