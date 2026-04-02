a = 1350051
ans = 0
while ans < 5:
    for i in range(111,a,100):
        if a % i == 0:
            print(a, i)
            ans += 1
            break
    a+=1


