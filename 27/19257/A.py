from math import dist

with open(r"C:\Users\vova55555\Desktop\Ege2026\27\19257\A.txt") as file:
    data = [list(map(float, a.replace(",",".").split())) for a in file]

def claster(c):
    R = []
    for dot in c:
        r = sum([dist(dot, doti) for doti in c])
        R.append([r, dot])
    return min(R)[1]

clastersi = [claster([i for i in data if i[1] < 5]), claster([i for i in data if i[1] > 5])]
print(int((clastersi[0][0] + clastersi[1][0])/2*10000),int((clastersi[0][1] + clastersi[1][1])/2*10000))

