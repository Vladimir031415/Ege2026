from math import dist

with open(r"C:\Users\vova55555\Desktop\Ege2026\27\19257\B.txt") as file:
    data = [list(map(float, a.replace(",",".").split())) for a in file]

def claster(c):
    R = []
    for dot in c:
        r = sum([dist(dot, doti) for doti in c])
        R.append([r, dot])
    return min(R)[1]

clastersi = [claster([i for i in data if i[0] < 0]), claster([i for i in data if i[0] > 0 and i[1] < 8]), claster([i for i in data if i[0] > 0 and i[1] > 8])]
print(int((clastersi[0][0] + clastersi[1][0] + clastersi[2][0])/3*10000),int((clastersi[0][1] + clastersi[1][1]+ clastersi[2][1])/3*10000))

