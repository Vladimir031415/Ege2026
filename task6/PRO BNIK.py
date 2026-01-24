for i in range(10,40):
    d = bin(i)[2:]

    if i%3 == 0:
        d += d[len(d)-3: len(d)]
    else:
        d += bin((i%3)*3)[2:]
    R = int(d,2)
    print(i,R)
