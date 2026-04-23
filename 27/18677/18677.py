from math import dist

with open(r"C:\Users\vova1\PycharmProjects\Ege2026\27\18677\27A_18677.txt") as file:
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
P1 = (centers[0][0] + centers[1][0])/2
P2 = (centers[0][1] + centers[1][1])/2
print(int(P1 * 100000),int(P2 * 100000))


with open(r"C:\Users\vova1\PycharmProjects\Ege2026\27\18677\27B_18677.txt") as file:
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
P3 = (centers[0][0] + centers[1][0] + centers[2][0])/3
P4 = (centers[0][1] + centers[1][1] + centers[2][1])/3
print(int(P3 * 100000),int(P4 * 100000))
