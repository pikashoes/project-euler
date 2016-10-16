# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 18:38:21 2016

@author: pikashoes

Question:
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

#This is O(n^2)
def findPalindrome():
    largestSoFar = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            y = i * j
            x = str(y)
            mid = int(len(x)/2)
            if (len(x) % 2) == 0: #If even number of digits
                if x[:mid] == x[len(x):mid - 1:-1]:
                    if y > largestSoFar:
                        largestSoFar = y
            else: #If odd number of digits
                if x[:mid + 1] == x[len(x):mid - 1:-1]: #Include the middle in both
                    if y > largestSoFar:
                        largestSoFar = y
    return largestSoFar
    

#To test:
#string = "Helloo"
#back = string[len(string):int(len(string)/2) - 1:-1]
#print(back)

print(findPalindrome())
#This gives us 906609
