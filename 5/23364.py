def tr(a):
    r = ""
    while a:
        r += str(a%3)
        a//=3
    return r[::-1]

for i in range(2, 100):
    t = tr(i)
    if i%3==0:
        t = "1" + t + "02"
    else:
        t = t + tr(4*(i%3))
    if int(t, 3) < 100:
        print(i)