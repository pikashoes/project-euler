# -*- coding: utf-8 -*-
"""
Solved: 12-25-2016

@author: pikashoes

Problem 5 Project Euler
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder. What is the smallest positive number
that is evenly divisible by all of the numbers from 1 to 20?
"""
from math import gcd

#THOUGHT PROCESS:
#------------------
#We are finding the smallest common multiple.
#Prime numbers are 2, 3, 5, 7, 11, 13, 17, 19.
#EUCLIDEAN ALGORITHM finds greatest common denominator
#def smallestnum():
#    start = 20
#    for i in range(1, 21):
#        while(start % i == 0):
#            continue
#        start += 20 #Increment by 20, since we know it has to be divisible by 20
#    return start
#
#print(smallestnum())

#THIS TAKES TOO LONG
#Maybe divide and conquer? It probably has to do with prime numbers.
#def smallestnumFaster(givenList, p, q):
#    mid = (p + q)/2
#    smallestnumFaster(givenList, p, mid)
#    smallestnumFaster(givenList, mid + 1, q)
#    getMultiple(givenList, p, mid, q)
#        
#
#prime = [2, 3, 5, 7, 11, 13, 17, 19]
#print(smallestnumFaster(prime, 0, 7)) 

def anotherWay(i, j): #i < j
    x = lcm(i, j)
    print(x)
    while i > 0:
        i -= 1
        anotherWay(i, x)
    return x

def lcm(a,b):
    return (a*b // gcd(a,b))

    
print(anotherWay(1, 2))