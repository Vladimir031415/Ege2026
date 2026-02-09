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
for N in range(6086056, 10**8):
    if c == 5:
        break
    dels = fact(N)
    if len(dels) == 2:
        if str(dels[0]).count("6") == str(dels[1]).count("6") == 1:

            print(N, max(dels))
            c+=1