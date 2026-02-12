cnt = 0

for a1 in range(1,15):
    for a2 in range(15):
        for a3 in range(15):
            for a4 in range(15):
                for a5 in range(15):
                    C = [a1, a2, a3, a4, a5]
                    if len(set(C)) == 2:
                        if C[4] == 0 or C[4] == 3:
                            cnt +=1
print(cnt)