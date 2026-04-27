
from itertools import combinations
from math import dist

def center(cluster):
    res = []
    for d1 in cluster:
        sd = sum([dist(d1,d2) for d2 in cluster])
        res.append([sd, d1])
    return min(res)[1]

with open(r"C:\Users\vova1\PycharmProjects\Ege2026\27\29080\27_A_29080.txt") as file:
    dots = []
    target = []
    for i in file:
        x,y, data = i.replace(",", ".").split()
        dots.append(list(map(float, [x,y])))
        if data[0] == "L" and data[1] == "3":
            target.append(dots[-1])

cluster1 = [[d for d in dots if d[1] > 8],[d for d in target if d[1] > 8]]
cluster2 = [[d for d in dots if d[1] < 8],[d for d in target if d[1] < 8]]

clusters = [cluster1, cluster2]
#print(len(cluster1[0]), len(cluster2[0]))
#print(len(cluster1[1]), len(cluster2[1]))
A1 = max(dist(center(cluster1[0]), d) for d in cluster2[1])
A2 = max(dist(center(cluster2[0]), d) for d in cluster1[1])

print(int(A1 *10000),int(A2 *10000))

with open(r"C:\Users\vova1\PycharmProjects\Ege2026\27\29080\27_B_29080.txt") as file:
    dots = []
    target = []
    for i in file:
        x,y, data = i.replace(",", ".").split()
        dots.append(list(map(float, [x,y])))
        if data[0] == "L" and data[1] == "3":
            target.append(dots[-1])

cluster1 = [[d for d in dots if d[1] > 23],[d for d in target if d[1] > 23]]
cluster2 = [[d for d in dots if 16< d[1] < 23],[d for d in target if 16 < d[1] < 23]]
cluster3 = [[d for d in dots if d[1] < 16],[d for d in target if d[1] < 16]]
clusters = [cluster1, cluster2, cluster3]
#print(len(cluster1[1]), len(cluster2[1]), len(cluster3[1]))
B1 = dist(center(cluster1[0]), center(cluster3[0]))
B2 = max([max(dist(d1,d2) for d1 in cluster1[1] for d2 in cluster3[1]), max(dist(d1,d2) for d1 in cluster2[1] for d2 in cluster3[1])])
print(int(B1 *10000),int(B2 *10000))