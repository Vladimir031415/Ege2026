a = 700000
cnt = 0
while cnt <= 5:
    for i in range(1, 300):
        if a % (i*10 +7) == 0:
            print(a,(i*10)+7)
            cnt += 1
            break
    a+=1