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
    
print(eratosthenes(1000))