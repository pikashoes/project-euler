while True:
    r = input("Enter a number: ")
    if r.isalpha():
        print("ERROR: Not a number.")
    elif (not r.isdigit()):
        print ("ERROR: Not a positive integer.")
    else:
        break

n = int(r)

def is_prime(n):
    if n > 1:
        for i in range (2, n):
            if (n % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False            

def factors(n):
   print("The prime factors of",n,"are:")
   for i in range(1, n + 1):
       if n % i == 0 and is_prime(i):
           print(i)

factors(n)

