def F(n):
    if n<10:
        return n
    else:
        if n%3 == 0:
            t = n%3 + 9
        else:
            t = n%3 + 6
    y = 0
    G = int((n - t)/3)
    for i in range(G):
        y+= t + (i+1)*3
    return y





print((F(6250)+2*F(6244))/F(6238))