# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 11:04:21 2015

@author: sya236
"""


L, t_max, p_max = 1000, 0, 0  #L must be an even integer

for p in range(L//4*2, L+1, 2):
    t = 0
    for a in range(2, int(p/3.4142) + 1):
        if  p*(p - 2*a) % (2*(p - a)) == 0: 
            t += 1
            if t >= t_max: t_max, p_max = t, p
 
print ("Maximum perimeter, p <=",L,"is", p_max)
print ("Triangles in set =", t_max)