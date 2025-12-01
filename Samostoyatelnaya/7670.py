for i in range(1, 1000):
    N = hex(i)[2:]
    N = N.replace("a","1")
    k = 0
    for j in N:
        if int(j, 16) % 2 == 0:
            k += 1
    if k > 2:
        R = N + "b"
    else:
        R = N + "f"
    if int(R, 16) > 3500:
        print(i)
        break
