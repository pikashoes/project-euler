def find_greatest_product(start, current):
    largest = current
    end = start + 12
    if end >= 1000:
        print(current)
        return current
    
    if "0" in d_number[start:end + 1]:
        find_greatest_product(end + 1, largest)
    else:
        product = 1
        for i in range(start, end + 1):
            product *= int(d_number[i])
        if product > current:
            largest = product
        find_greatest_product(start + 1, largest)

print(find_greatest_product(0, 0))