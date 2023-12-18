#generate list of primes
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
#generate the list of squbes made from primes less than x, which are less than z
def squbes(x,z):
    squbes_list = []
    pl = eratosthenes(x)
    for x in pl:
        for y in pl:
            if x != y and x**2 * y**3 <= z: 
                squbes_list.append(x**2 * y**3)
    squbes_list.sort()
    return(squbes_list)
#make a new list from the sques one inwhich every element has a string involving "200"
def two_hundredinator(list):
    lista = [str(x) for x in list]
    matching = [x for x in lista if "200" in x]
    listb = [int(x) for x in matching]
    return(listb)
#generate a new list of elements which are not prime no matter which digit is changed
def digit_list(x):
    dl = []
    digits = ["1","2","3","4","5","6","7","8","9","0"]
    for i in range(len(x)):
        if x[i].isdigit():
            dl.extend([int(x[:i] + d + x[i+1:]) for d in digits])
    return dl
def digital_prime(list):
    lista = [str(x) for x in list]
    listb = [[int(x),digit_list(x)] for x in lista]
    return(listb)
#given any 
def isitprimea(list):
    finale = []
    v = digital_prime(list)
    for x in v:
        a, b = x
        z = [a for a in x]
        k = [i for i in range(1, max(z)+1)]
        u = k.remove(eratosthenes(max(z)))
        for y in b:
            if all(r in u for r in b):
                finale.append(a)
    return(finale)
