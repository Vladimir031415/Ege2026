with open(r'.\files\9778.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 1
for line in data:
    amount = [line.count(i) for i in set(line)]
    if sorted(amount) == [1,1,1,1,2]:
        pov = [i for i in line if line.count(i) > 1]
        nepov = [i for i in line if line.count(i) == 0]
        if sum(nepov)/4  <= pov[0]:
            print(cnt)
            break
