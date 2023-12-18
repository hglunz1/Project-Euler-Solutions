import math

def i_sqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return(x)

def eratosthenes(x):
    spec_primes = []
    prime = [True for i in range(x+1)]
    p = 2
    while p**2 <= x:
        if prime[p] == True:
            for i in range(p*2, x+1, p):
                prime[i] = False
        p = p+1 if p == 2 else p+2
    for p in range(2,x+1):
        if prime[p]:
            spec_primes.append(p)
    return(spec_primes)
    
def factorizer(x):
    factors = []
    mset = eratosthenes(x//2)

    if x == 2:
        factors.append([2,1])
    if x == 3:
        factors.append([3,1])

    for p in mset:
        if x % p == 0:
            i = 0
            while x % p == 0:
                x = x//p
                i = i+1
            else:
                factors.append([p,i])

    if x>1:
        factors.append([x,1])

    return(factors)

def strong_check(x):
    strong = True
    s = factorizer(x)
    if x == 1:
        strong = False
    for m in s:
        a, b = m
        if b < 2:
            strong = False
    return(strong)

def phi(x):
    if x == 0:
        return(0)
    phin = x
    p = 2
    while p**2 <= x:
        if x % p == 0:
            phin = phin - phin//p
            while x % p == 0:
                x = x//p
        p = p+1
    if x > 1:
        phin = phin - phin//x
    return(phin)

def perfect_power(x):
    pp = False
    list = []
    m = factorizer(x)
    for u in m:
        a,b = u
        list.append(b)
    if math.gcd(*list) > 1:
        pp = True
    return(pp)

def achilles_strong(x):
    a_strong = []
    for n in range(1, x+1):
        if strong_check(n) == True and strong_check(phi(n)) == True and perfect_power(n) == False and perfect_power(phi(n)) == False:
            a_strong.append(n)
    return(a_strong)

print(achilles_strong(10**5))