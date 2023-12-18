import math

def naive_primes_less_than(x):
    set_of_primes = [2]
    set_of_not_primes = []
    z = 3
    while z <= int(x):
        i = 0
        possible_prime = True
        while i < len(set_of_primes):
            if z % set_of_primes[i] == 0:
                possible_prime = False
                break    
            i = i+1
        if possible_prime == False:
            set_of_not_primes.append(z)

        else:
            set_of_primes.append(z)
        z = z+1
    return (set_of_primes, set_of_not_primes)

def primes_less_than(x):
    set_of_primes = naive_primes_less_than(math.sqrt(x))[0]
    set_of_not_primes = naive_primes_less_than(math.sqrt(x))[1]
    bps = []
    z = 3
    while z <= int(x):
        if z < math.sqrt(x):
            z = z+1
        else:
            i = 0
            possible_prime = True
            while i < len(set_of_primes):
                if z % set_of_primes[i] == 0:
                    possible_prime = False
                    break    
                i = i+1
            if possible_prime == False:
                set_of_not_primes.append(z)
            else:
                bps.append(z)
            z = z+1

    for p in bps:
        set_of_primes.append(p)

    return(set_of_primes)
    
print(primes_less_than(1000000))