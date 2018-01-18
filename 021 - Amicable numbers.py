def amicable():
    answer = 0
    for a in range(10001):
        b = d(a)
        temp = d(b)
        if temp == a and a != b:
            print(a, b)
            answer += a
    return answer
        
def d(x):
    list_divisors = get_divisors(x)
    return sum(list_divisors)
    
def get_divisors(num):
    answer = []
    if (num == 1):
        return [1]
    else:
        for i in range(1, num):
            if (num % i) == 0:
                answer.append(i)
    return answer

print(amicable())