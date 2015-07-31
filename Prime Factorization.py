while True:
    r = input("Please enter a number:")
    if r.isalpha():
        print("ERROR: Not a number.")
    elif (not r.isdigit()):
        print ("ERROR: Not a positive integer.")
    else:
        break

number = int(r)

def factors(number):
    if number == 1:
        return []

    for i in range(2, number):
        qt, rd = divmod(number, i)
        if not rd:
            return [i] + factors(qt)

    return [number]

print (factors(number))
