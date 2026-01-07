

s = "1"*30 + "0"*45

def f(i, q):
    if i == 1:
        if q == 1:
            return [1, 2]
        if q == 2:
            return [0, 3]
        if q == 3:
            return [1, 1]
    if i == 0:
        if q == 1:
            return [0, 2]
        if q == 2:
            return [1, 3]
        if q == 3:
            return [0, 2]

s2 = ""
q = 1
for i in s:
    i = int(i)

    X = f(i,q)
    s2 += str(X[0])
    q = X[1]
print(s2)
r = 0
for i in s2:
    if i == "1":
        r += 1
print(r)


