#generate list of primes
def eratosthenes(x):
    primes = []
    prime = [True for i in range(x+1)]
    p = 2
    while p**2 <= x:
        if prime[p] == True:
            for i in range(p**2, x+1, p):
                prime[i] = False
        p = p+1 if p == 2 else p+2
    for p in range(2,x+1):
        if prime[p]:
            primes.append(p)
    return(primes)
#generate the list of semiprimes made from primes less than x, which are less than z
def semiprimes(x,z):
    semiprime_set = set()
    pl = eratosthenes(x)
    for i in range(len(pl)):
        for j in range(i,len(pl)):
            if pl[i]*pl[j] <= z: 
                semiprime_set.add(pl[i]*pl[j])
            else:
                break
    return(sorted(semiprime_set))

print(len(semiprimes(5*10**7,10**8)))