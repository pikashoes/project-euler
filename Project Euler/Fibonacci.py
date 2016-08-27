n = 4000000

f1 = 1
f2 = 1
add = 0
result = 0

while add < n:
   f1 = f2
   f2 = add   
   add = (f1 + f2)         
   if add % 2 == 0:
       result = result + add
       
print (result)
