n = 0
c = 700000
d =[]

def F(c):
    for i in range(1,40000):
        if c % (i*10 +7) == 0:
            d.append([c,i*10 +7])
            return True
    return False





while n < 5:
    c += 1
    if F(c) == True:
        n+=1
print(d)