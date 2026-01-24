ch = 0
N = 800000
while ch <= 10:
    for i in range(40002):
        if N % (i*10 + 9) == 0:
            print(N, i*10 + 9)
            ch+=1
    N+=1

