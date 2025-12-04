for i in range(2,20):
    N = bin(i)[2:]
    if N.count('1')%2 == 0:
        R = "10" + N[2:] + "0"
    else:
        R = "11" + N[2:] + "1"
    print(i, int(R,2))