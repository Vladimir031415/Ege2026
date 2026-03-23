def f1(line):
    am = [line.count(i) for i in line]
    return sorted(am) == [1,1,1,1,3]

def f2(line):
    pov = [i for i in line if line.count(i) > 1]
    nepov = [i for i in line if line.count(i) == 0]
    return sum(nepov)/len(nepov) <= pov[0]



with open(r'.\files\9740.txt') as file:
    data = [list(map(int, i.split())) for i in file]


cnt = 0
for i in data:
    if f1(i) and f2(i):
        print(cnt)
        break
