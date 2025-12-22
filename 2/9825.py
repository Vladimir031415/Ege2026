for w in 0,1:
    for x in 0,1:
        for y in 0,1:
            for z in 0,1:
                f = (x <= (z == w)) or not(y <= w)
                if f == 0:
                    print(w,x,y,z)