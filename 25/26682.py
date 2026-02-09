def de(num):
    a = []
    dels = fact(num)
    for i in set(dels):
        a += [dels.count(i)]

    r = 1
    for i in a:

        r *= (i+1)
    return r



def fact(num):
    d = []
    i = 2
    while i * i < num + 1:
        while num % i == 0:
            d+= [i]
            num //= i
        i += 1

    if num >= 2:
        d += [num]
    return d

c = 0
for N in range(5200_000, 10**8):
    if c == 5:
        break
    dels = fact(N)
    if len(dels) == 9:
        if de(N) % 90 == 0:

            print(N, max(dels))
            c+=1