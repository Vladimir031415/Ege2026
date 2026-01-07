def f1(S):
    t = 0
    for i in S:
        if i %2 == 1:
            t+= 1
    if t == 1:
        return True
def f2(S):
    t = 0
    for i in S:
        if i <= 5:
            t+=1
    if t <= 2:
        return True
u = []
k = 0
for a in range(1, 25):
    for b in range(25):
        for c in range(25):
            for d in range(25):
                S = [a,b,c,d]
                if f1(S) and f2(S) == True:
                    k += 1


print(k)
