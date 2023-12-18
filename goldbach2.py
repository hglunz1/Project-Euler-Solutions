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

def list_squares(x):
    u = 0
    squares = []
    while u*u <= x:
        squares.append(u*u)
        u = u+1
    return(squares)

def odd_numb(x):
    u = 1
    odd = []
    while u <= x:
        odd.append(u)
        u = u+2
    return(odd)

def goldbach2(x):
    gold_list = []
    p = primes_less_than(x)
    s = list_squares(x)
    n = odd_numb(x)
    i = 0
    while i < len(p):
        j = 0
        while j < len(s):
            gold_list.append(2*s[j]+p[i])
            j = j+1
        i = i+1
    print(list(set(n) - set(gold_list)))

goldbach2(100000)


