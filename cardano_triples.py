import math

def triple_generator(x):
    triples = []
    for i in range(1,x):
        for j in range(i+1,x):
            triples.append([i,j-i,x-j])
    return(triples)

def cardano_checker(a,b,c):
    return 8*a**3 + 15*a**2 + 6*a - 27*b**2*c == 1

def tgcc(x):
    ts = []
    for v in range(1,x+1):
        tv = triple_generator(v)
        for u in tv:
            a, b, c = u
            if cardano_checker(a,b,c) == True:
                ts.append([a,b,c])
    return(ts)

print(len(tgcc(1000)))