def p(num):
    if num < 2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True

def f(num):
    d = []
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            if p(i): d += [i]
            if p(num//i): d += [num//i]
    if len(d) == 12:
        return max(d)
    return 0

a = 24517512
cnt = 0
for N in range(a+1, 10**10):
    M = f(N)
    if M:
        print(N,M)
        cnt += 1
        if cnt == 5:
            break