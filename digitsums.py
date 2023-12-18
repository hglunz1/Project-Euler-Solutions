def sum_of_digits(n):
    u = sum(int(digit) for digit in str(n))
    return(u)
    
set = []
a = 0
while a <=100:
    b = 0
    while b <= 100:
        set.append([a, b, sum_of_digits(a**b)])
        b = b+1
    a = a+1

for v in set:
    max_3 = max(v[2] for v in set)
    w = [m for m in set if m[2]== max_3]
print(w)