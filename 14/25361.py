with open("24_25361.txt") as text:
    data = text.readline()
i =

for i in range(len(data)):
    if data[i] in "02468":
        f = 0
        r = 0
        for j in data[i:]:
            if j not in "02468":
                if f <= 76:
                    if j == "f":
                        f+=1
                    r+=1
                else:
                    if i >= 100:
                        print(i)
                    break
            else:
                if i >= 100:
                    print(i)

                break
print(r)







