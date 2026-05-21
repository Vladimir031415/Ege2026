from math import dist

with open(r"C:\Users\vova1\PycharmProjects\Ege2026\27\23209\27_A_23209.txt") as file:
    data = [list(map(float, a.replace(",",".").split())) for a in file]


def center(cluster):
    res = []
    for d1 in cluster:
        sd = sum([dist(d1,d2) for d2 in cluster])
        res.append([sd, d1])
    return min(res)[1]

clA1 = [dot for dot in data if dot[0] < 5]
clA2 = [dot for dot in data if dot[0] > 5]
center_A1 = center(clA1)
center_A2 = center(clA2)

print(max([center_A1[0],center_A2[0]]) * 10000)
print(max([center_A1[0],center_A2[0]]) * 10000)

with open(r"C:\Users\vova1\PycharmProjects\Ege2026\27\23209\27_B_23209.txt") as file:
    data = [list(map(float, a.replace(",",".").split())) for a in file]

clB1 = [dot for dot in data if 3 < dot[1] < 12]
clB2 = [dot for dot in data if 15 < dot[0] < 21]
clB3 = [dot for dot in data if 21 < dot[0] < 27]
cl = [clB1,clB2,clB3]
ma = center(max(cl, key=len))
mi = center(min(cl, key=len))

print[mi[0], ma[0]]


