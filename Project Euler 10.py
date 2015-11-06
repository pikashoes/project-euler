import time
start = time.clock()

def sumPrimes(n):
    s = 0
    x = [True] * (n+1)
    for p in range(2, n):
        if x[p]:
            s += p
            for i in range(p*p, n, p):
                x[i] = False
    return s

print (sumPrimes(2000000))

elapsed = time.clock() - start
print (elapsed)
