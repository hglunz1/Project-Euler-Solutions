def divisors(x):
    divisors_set = set()
    ds2 = set()
    for y in range(1,x):
        if y*y <= x:
            if x % y == 0:
                divisors_set.add(y)
        else:
            break
    for y in divisors_set:
        ds2.add(x // y)
    for z in ds2:
        divisors_set.add(z)
    return(sorted(divisors_set))

def pseudo_square_root(x):
    ppsr = []
    u = divisors(x)
    for v in u:
        if v*v <= x:
            ppsr.append(v)
    return(max(ppsr))

def eratosthenes(x):
    primes = []
    prime = [True for i in range(x+1)]
    p = 2
    while p**2 <= x:
        if prime[p] == True:
            for i in range(p*2, x+1, p):
                prime[i] = False
        p = p+1 if p == 2 else p+2
    for p in range(2,x+1):
        if prime[p]:
            primes.append(p)
    return(primes)

def build_a_number(x):
    u = eratosthenes(x)
    num = 1
    for i in range(0, len(eratosthenes(x))):
        num = num * u[i]
    return(num)

print(pseudo_square_root(build_a_number(30)))
print(build_a_number(30))
print(79534**2)
print(build_a_number(30)-79534**2)