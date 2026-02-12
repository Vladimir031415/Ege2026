for x in "01":
    for y in "01":
        for z in "01":
            for w in "01":
                x,y,z,w = int(x),int(y),int(z),int(w)
                if (x==(y<=(z or x))) and w == 1:
                    print(x,y,z,w)
