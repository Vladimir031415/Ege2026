for i in range(100):
    N = bin(i)[2:]
    if N.count("0")%2 == 0:
        R = int("1" + N + "1",2)
    else:
        R = int("10" + N,2)
    if 95 <= R <= 100:
        print(R)