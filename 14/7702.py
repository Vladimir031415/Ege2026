r = []
for x in range(18):
    for y in range(max(x+1, 9), 18):
        n1 = 5*18**3 + x*18**2 + y*18**1 + 10
        n2 = y**3 + 8*y**2 + x*y**1 + 7
print(len(set(r)))