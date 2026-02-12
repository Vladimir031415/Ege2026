def p(a):
    if a < 2:
        return False
    else:
        for i in range(2,int(a**.0)+1):
            if a%i == 0:
                return False
        return True

def fact(num):
    d = []
    i = 3
    while i < int(num ** .5) + 1:
        while num % i:
            d+= [i]
            num //= i

        if num > 2:
            d += [i]
    return d

for N in range(5_000_001, 10**10, 2):
    dels = fact(N)
    if len(dels) == 2 and dels[0] != dels[1]:
        if p(dels[1]-dels[0]):
            print(N, dels[1]-dels[0])
