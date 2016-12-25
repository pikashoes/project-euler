# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 15:20:08 2016

@author: pikashoes
"""

import csv, sys, os

f = open('mannadonors.csv')
csv_f = csv.reader(f)

final_file = []

for row in csv_f:
    row[0] = row[0].replace('(deleted)', '')
    final_file.append(row)

out_name = 'mannadonorsEDITED.csv'
a = open(out_name, 'w')
writer = csv.writer(a)
writer.writerows(final_file)
a.close()