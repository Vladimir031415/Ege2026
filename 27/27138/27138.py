from math import dist

with open(r"C:\Users\vova1\PycharmProjects\Ege2026\27\27138\27A_27138.txt") as file:
    dots = [list(map(float, a.replace(",",".").split())) for a in file]


def center(cluster):
    res = []
    for d1 in cluster:
        sd = sum([dist(d1,d2) for d2 in cluster])
        res.append([sd, d1])
    return min(res)[1]

eps = 1
clusters = []
while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cluster.append(d)
                dots.remove(d)
    if len(cluster) > 30:
        clusters.append(cluster)

centers = [center(cluster) for cluster in clusters]
print([len(cluster) for cluster in clusters])
Sx = abs(centers[0][0] - centers[1][0])
Sy = abs(centers[0][1] - centers[1][1])
print(int(abs(Sx) * 10000),int(abs(Sy) * 10000))


with open(r"C:\Users\vova1\PycharmProjects\Ege2026\27\27138\27B_27138.txt") as file:
    dots = [list(map(float, a.replace(",",".").split())) for a in file]



def center(cluster):
    res = []
    for d1 in cluster:
        sd = sum([dist(d1,d2) for d2 in cluster])
        res.append([sd, d1])
    return min(res)[1]


eps = 1
clusters = []
while dots:
    cluster = [dots.pop()]
    for dot in cluster:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cluster.append(d)
                dots.remove(d)

    if len(cluster) > 30:
        clusters.append(cluster)

print([len(cluster) for cluster in clusters])
Q1 = max(clusters[2])[0]
centers = [center(cluster) for cluster in clusters]

Q = []
for d1 in clusters[0]:
    for d2 in clusters[1]:
        Q.append([dist(d1,d2), d1[0]+d1[1]])
    for d2 in clusters[2]:
        Q.append([dist(d1,d2), d1[0]+d1[1]])

for d1 in clusters[1]:
    for d2 in clusters[2]:
        Q.append([dist(d1,d2), d1[0]+d1[1]])
    for d2 in clusters[0]:
        Q.append([dist(d1,d2), d1[0]+d1[1]])

for d1 in clusters[2]:
    for d2 in clusters[0]:
        Q.append([dist(d1,d2), d1[0]+d1[1]])
    for d2 in clusters[1]:
        Q.append([dist(d1,d2), d1[0]+d1[1]])

Q2 = max(Q)[1]
print(int(abs(Q1)*10000), int(abs(Q2)*10000))
