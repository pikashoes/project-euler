# -*- coding: utf-8 -*-
"""
Solved: 10-31-2017, 15:09
https://projecteuler.net/problem=13
"""

f = open('013sup.txt', 'r')

final_num = 0
for line in f:
    final_num += int(line)

string_final = str(final_num)
print(string_final[:10])