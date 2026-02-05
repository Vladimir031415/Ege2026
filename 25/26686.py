def p(a):
    if a < 2:
        return False

    for i in range(2,int(a**.5)+1):
        if a%i == 0:
            return False
    return True

def fact(num):
    d = []
    i = 2
    while i < int(num ** .5) + 1:
        while num % i:
            d+= [i]
            num //= i
        i += 1

    if num >= 2:
        d += [i]
    return d
c = 0
for N in range(89_428_305, 10**10):
    if c == 7:
        break
    dels = fact(N)
    if len(dels) >= 6:
        if N%sum(dels)==0:
            print(N, sum(dels))
            c+=1
