from math import dist

with open(r"C:\Users\vova1\PycharmProjects\Ege2026\27\23384\27_A_23384.txt") as file:
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

centers = [center(cluster) for cluster in clusters]
print(int(sum(cent[0] for cent in centers) * 10000), int(sum(cent[1] for cent in centers) * 10000))

with open(r"C:\Users\vova1\PycharmProjects\Ege2026\27\23384\27_B_23384.txt") as file:
    dots = [list(map(float, a.replace(",",".").split())) for a in file]

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

centers = [center(cluster) for cluster in clusters]
print(int(max((cent[0]**2 + cent[1]**2)**.5 for cent in centers) * 10000), int(max((cent[0]**2 + cent[1]**2)**.5 for cent in centers) * 10000))
