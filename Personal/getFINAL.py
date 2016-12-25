# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 15:37:17 2016

@author: pikashoes
"""

import csv
from string import whitespace

def main():
    f = open('donors.csv', 'r')
    csv_f = csv.reader(f)
    
    x = open('mannaemailalum.csv', 'r')
    csv_x = csv.reader(x)
    
    y = open('mannaemailnotalum2.csv', 'r')
    csv_y = csv.reader(y)
    
    final_file = []
    names = {}
    notalum = {}
    
    for line in csv_x:
#        print("hello!!")
        line_edit = line[0].translate(dict.fromkeys(map(ord, whitespace)))
        line_edit = line_edit.replace("-", "")
        line_edit = line_edit.replace(".", "")
        names[line_edit] = [line[1], line[2]]
        
    for line in csv_y:
#        print("hello")
        line_edit = line[0].translate(dict.fromkeys(map(ord, whitespace)))
        line_edit = line_edit.replace("-", "")
        line_edit = line_edit.replace(".", "")
        notalum[line_edit] = line[1]
    
#    print(names)
    
    for row in csv_f:
        line_edit = row[0].translate(dict.fromkeys(map(ord, whitespace)))
        line_edit = line_edit.replace("-", "")
        line_edit = line_edit.replace(".", "")
        
        if line_edit in names.keys():
            final_file.append([row[0], names.get(line_edit)[0], names.get(line_edit)[1]])
        elif line_edit in notalum.keys():
            final_file.append([row[0], notalum.get(line_edit)])
        else:
            final_file.append(row)
    
    out_name = 'donors2016EDITED.csv'
    a = open(out_name, 'w')
    writer = csv.writer(a)
    writer.writerows(final_file)
    a.close()

#def checkSame(str1, str2):
#    if str1 == str2:
#        return True
#    else:
#        return False

main()