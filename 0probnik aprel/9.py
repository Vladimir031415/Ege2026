with open(r"C:\Users\vova55555\Desktop\Ege2026\0probnik aprel\9.txt") as file:
    data = [list(map(int, i.split())) for i in file]

n = 1

for i in data:
    if len(set(i)) == 5:
        print(i)
        p = [j for j in i if i.count(j) == 2][0]
        print(p)
        if p >= (sum(i) - 2 * p)/4:
            print(n)
            break
    n += 1
