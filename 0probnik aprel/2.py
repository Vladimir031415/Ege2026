def f(w,x,y,z):
    return ((z==x) <= w) and (w<=(y and x))
for w in 0, 1:
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                if f(w,x,y,z):
                    print(w,x,y,z)