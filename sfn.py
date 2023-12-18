def sf(x):
    sf = True
    m = 2
    while m**2<=x:
        if x % m**2 == 0:
            sf = False
            break
        else:
            m = m+1
    return(sf)

def checker(x):
    list = []
    for n in range(1,x+1):
        if sf(n**2+1) == True:
            list.append(n)
    return(list)

print(len(checker(12345)))