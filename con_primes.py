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

def consecutive_primes(x):
    cp = []
    set = primes_less_than(x)
    for u in set:
        if u+2 in set:
            cp.append([u, u+2])
    return(cp)

def sum_function(x):
    our_sums = []
    tps = consecutive_primes(x)
    tps.remove([3, 5])
    for pair in tps:
        p_1, p_2 = pair
        k = 0
        while (p_1+(10**(len(str(p_1))))*k) % p_2 != 0:
            k = k+1
        else:
            our_sums.append([p_1, p_2, p_1+(10**(len(str(p_1))))*k])
    return(our_sums)

def sums(x):
    v = sum_function(x)
    fill = []
    for b in v:
        a_1, a_2, a_3 = b
        fill.append(a_3)
    return(sum(fill))

print(consecutive_primes(100000))