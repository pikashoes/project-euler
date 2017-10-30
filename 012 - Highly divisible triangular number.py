# -*- coding: utf-8 -*-
"""
Soleved: 10-30-2017, 15:31

Question:
What is the value of the first triangle number to have over five hundred divisors?
"""
import time, EulerHelpers

#Main
def triangle():
    nth = 1
    current = 1
    found = False
    while not found:
        if EulerHelpers.count_divisors(current) > 500:
            return current
        else:
            current += (nth + 1)
            nth += 1

start = time.clock()
print(triangle())
end = time.clock()
total_time = end - start

print("Time taken: " + str(total_time))