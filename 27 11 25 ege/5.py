for i in range(10,1000):
    N = bin(i)[2:]
    if sum(map(int, list(N))) % 2 == 0:
        R = "11" + N[2:] + "1"
    else:
        if N.count("0") < N.count("1"):
            R = N + "0"
        else:
            R = N + "1"
#    print(int(R,2))
    if int(R,2)>271:
        print(i)
        break
