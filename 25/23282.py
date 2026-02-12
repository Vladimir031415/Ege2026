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
            if p(i): d |= {i}
            if p(num//i): d |= {num//i}
    if len(d) >= 2:
        M = max(d) + min(d)
        if M > 60_000 and str(M) == str(M)[::-1]:
            return M
    return 0

cnt = 0
for N in range(5400001, 10**7):
    if M := f(N):
        print(N, M)
        cnt += 1
        if cnt == 5:
            break
