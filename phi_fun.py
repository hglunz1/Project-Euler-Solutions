import math
def gcd(p,q):
    while q != 0:
        p, q = q, p%q
    return p

def is_coprime(x, y):
    return gcd(x, y) == 1

def phi_func(x):
    if x == 1:
        return 1
    else:
        n = [y for y in range(1,x) if is_coprime(x,y)]
        return len(n)

def phi_counting(x,y):
    list = []
    n = 0
    while len(list) < y and n<x**2:
        if x == phi_func(n):
            list.append(n)
        n = n+1
    return(list)
    
print(phi_counting(math.factorial(8),2))