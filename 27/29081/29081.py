
from itertools import combinations
from math import dist

def center(cluster):
    res = []
    for d1 in cluster:
        sd = sum([dist(d1,d2) for d2 in cluster])
        res.append([sd, d1])
    return min(res)[1]

with open(r"C:\Users\vova1\PycharmProjects\Ege2026\27\29081\27_A_29081.txt") as file:
    dots = []
    target = []
    for i in file:
        x,y, data = i.replace(",", ".").split()
        dots.append(list(map(float, [x,y])))
        if data[2:] == "VII":
            target.append(dots[-1])

cluster1 = [[d for d in dots if d[1] > 8],[d for d in target if d[1] > 8]]
cluster2 = [[d for d in dots if d[1] < 8],[d for d in target if d[1] < 8]]

clusters = [cluster1, cluster2]
centers = [center(cluster1[0]), center(cluster2[0])]
A1 = min([min(dist(centers[0], d1) for d1 in clusters[0][1]), min(dist(centers[1], d1) for d1 in clusters[1][1])])
A2 = max([max(dist(centers[0], d1) for d1 in clusters[0][1]), max(dist(centers[1], d1) for d1 in clusters[1][1])])

with open(r"C:\Users\vova1\PycharmProjects\Ege2026\27\29081\27_B_29081.txt") as file:
    dots = []
    target = []
    for i in file:
        x,y, data = i.replace(",", ".").split()
        dots.append(list(map(float, [x,y])))
        if data[1] >= "8":
            target.append(dots[-1])

cluster1 = [[d for d in dots if d[1] > 23],[d for d in target if d[1] > 23]]
cluster2 = [[d for d in dots if 16< d[1] < 23],[d for d in target if 16 < d[1] < 23]]
cluster3 = [[d for d in dots if d[1] < 16],[d for d in target if d[1] < 16]]

clusters = [cluster1, cluster2, cluster3]

B1 = min([dist(d1, d2) for cl1,cl2 in combinations(clusters, 2) for d1 in cl1[1] for d2 in cl2[1]])
ans = [dist(d1,d2) for c in clusters for d1, d2 in combinations(c[1], 2)]
B2 = sum(ans) / len(ans)
print(int(A1 *10000),int(A2 *10000))
print(int(B1 *10000),int(B2 *10000))
