def int100(a):
    t = 0
    R = 0
    for i in a[::-1]:
        R += int(i,20)*100**t
        t+=1
    return(R)


for x in range(100):
    a = int100("7A00123")+x*100**4 - (int100("1BA640") + x) + int100("98012C") + x*100**6
    if a % 21 == 0:
        print(x)


