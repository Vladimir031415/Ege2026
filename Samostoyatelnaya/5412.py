a = 0
for i in range(1, 1000):
    N = hex(i)[2:]
    k = 0
    for j in N:
        if j == "b":
            k += 1
    if k > 2:
        R = "1"+ N
    else:
        R = N + "1"
    if 9 < int(R, 16) < 100 :
        a+=1
print(a)