with open(r"C:\Users\vova55555\Desktop\Ege2026\27\17882\27_A_17882.txt") as file:
    dots = [list(map(float, a.split())) for a in file]

from math import dist

def center(cluster):
    res = []
    for d1 in cluster:
        sd = sum([dist(d1,d2) for d2 in cluster])
        res.append([sd, d1])
    return min(res)[1]

cl1 = [dot for dot in dots if dot[1] < 3]
cl2 = [dot for dot in dots if dot[1] > 3]
center_1 = center(cl1)
center_2 = center(cl2)

print((center_1[0]+center_2[0])/2 * 10000)
print((center_1[1]+center_2[1])/2 * 10000)