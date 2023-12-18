import math
def square_free(x):
    possible_sf = True
    k = 2
    while k <= math.sqrt(x):
        if x % k**2 != 0:
            possible_sf = True
            k = k+1
        else:
            possible_sf = False
            break
    return(possible_sf)

def binomail_list(x):
    list = []
    n = 1
    k = 0
    while n <= x:
        k = 0
        while k <= n:
            list.append([n, k, math.comb(n,k)])
            k = k+1
        n = n+1
    return(list)

def sfsq_list(x):
    new_list = []
    bin = binomail_list(x)
    for comb in bin:
        n, k, nCk = comb
        if square_free(nCk) == True and nCk != 1:
            new_list.append(comb)
    return(new_list)


print(sfsq_list(51))