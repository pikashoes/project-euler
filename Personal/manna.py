# -*- coding: utf-8 -*-
"""
Created on Tue May  3 12:52:01 2016

@author: pikashoes
"""

import sys, os, csv
file = sys.argv[-1] #The last argument in the command line will be the file.

locations = ["MO", "GA", "DC", "PA", "TX", "CT", "OH", "MI", "DE", "FL",
             "CA", "NY", "NJ", "VA", "MD", "IL", "MA", "HI", "WA", "AU",
             "NM", "NC", "WI", "LA", "NH"]

#Open the file
with open(file, 'r+') as f:
    final_file = []
    path = os.path.dirname(file)
    
    for line in f:
        eachrow = []
        newline = line.split(",")
        location = newline[-1]
        state = location[1:3]
        if state in locations:
            eachrow.append(newline[0])
            eachrow.append(newline[-2])
            eachrow.append(state)
            eachrow.append(newline[1])
        final_file.append(eachrow)

    out_name = 'outMannanew.csv'
    outputFile = os.path.join(path, out_name)   
    a = open(outputFile, 'w')
    writer = csv.writer(a)
    writer.writerows(final_file)
    a.close()