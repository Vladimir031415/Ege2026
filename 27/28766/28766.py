from math import dist

with open(r"C:\Users\vova1\PycharmProjects\Ege2026\27\28766\27_A_28766.txt") as file:
    dots = []
    target = []
    for i in file:
        x,y, data = i.replace(",", ".").split()
        dots.append(list(map(float, [x, y])))
        if data[0] == "Y" and data[2:].rstrip() == "III":
            target.append(list(map(float, [x, y])))



def center(cluster):
    res = []
    for d1 in cluster:
        sd = sum([dist(d1,d2) for d2 in cluster])
        res.append([sd, d1])
    return min(res)[1]

cluster_1 = [d for d in dots if d[1] < 8]
cluster_2 = [d for d in dots if d[1] > 8]

center1 = center(cluster_1)
center2 = center(cluster_2)



distR = [dist(center2, R) for R in target]

print(int(min(distR) * 10000),int(max(distR) * 10000))


with open(r"C:\Users\vova1\PycharmProjects\Ege2026\27\28766\27_B_28766.txt") as file:
    dots = []
    target = []
    for i in file:
        x,y, data = i.replace(",", ".").split()
        dots.append(list(map(float, [x, y])))
        if data[0] == "Z" and data[2:].rstrip() == "I":
            target.append(list(map(float, [x, y])))

cluster_1 = [[d for d in dots if d[1] < 16], [d for d in target if d[1] < 16]]
cluster_2 = [[d for d in dots if 16 < d[1] < 22], [d for d in target if 16 < d[1] < 22]]
cluster_3 = [[d for d in dots if 22 < d[1]], [d for d in target if 22 < d[1]]]
center1 = center(cluster_1[0])
center2 = center(cluster_2[0])
center3 = center(cluster_3[0])

B2 = dist(center1, center2)

def minrast_mejdu(cluster):
    m = []
    for d1 in cluster:
        for d2 in cluster:
            if d1 != d2:
                m.append(dist(d1,d2))
    if len(m) != 0:
        return min(m)
    else:
        return 10000

B1 = min([minrast_mejdu(cluster_1[1]),minrast_mejdu(cluster_2[1]),minrast_mejdu(cluster_3[1])])

print(int(B1 * 10000),int(B2 * 10000))