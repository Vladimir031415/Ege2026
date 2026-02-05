def sp(a):
    r = []
    for i in range(2,int(a**.5)+1):
        if a % i == 0:
            r.append(i)
            r.append(a//i)
    if len(r) != 0:
        return sum(r)//len(r)
    else:
        return 0

cnt = 0
a = 5
while cnt < 7:
    if sp(a)%1000 == 313:
        print(a,sp(a))
        cnt += 1
