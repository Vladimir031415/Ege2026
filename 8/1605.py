r = 0
for N in range(100):
    R = bin(N+2)[2:]
    R += str(sum(map(int, list(R))) % 2)
    R += str(sum(map(int, list(R))) % 2)
    if int(R, 2)<=61:
        r = N
print(r)