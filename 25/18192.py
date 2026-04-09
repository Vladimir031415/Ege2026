def fact(n):
    mn = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            mn.append(i)
            n = n // i
        i += 1
    if n > 1: mn.append(n)
    return mn
ans = 0
a = 1000001
while ans < 5:
    if len(fact(a)) == 3:
        print(a, max(fact(a)))
        ans += 1
    a += 1
