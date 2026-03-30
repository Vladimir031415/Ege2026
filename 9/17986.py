print(len([i for i in [list(map(int, i.split())) for i in open(r"C:\Users\vova1\PycharmProjects\Ege2026\9\files\17986.txt")] if (max(i) < sum(i) - max(i)) and sum([j for j in i if j % 2]) == sum([j for j in i if j % 2 == 0])]))

