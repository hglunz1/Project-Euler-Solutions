from tabulate import tabulate
import math

def eratosthenes(x):
    primes = []
    prime = [True for i in range(x+1)]
    p = 2
    while p**2 <= x:
        if prime[p] == True:
            for i in range(p**2, x+1, p):
                prime[i] = False
        p = p+1
    for p in range(2,x+1):
        if prime[p]:
            primes.append(p)
    return(primes)

data = [["x", "p(X)", "X/log(X)"], [10**8,len(eratosthenes(10**8)),float(10**8/math.log(10**8))]]

print(tabulate(data, headers='keys'))