with open(r'..\files\26_5066.txt') as file:
    N = int(file.readline())
    containers = [i.split() for i in file]

containers = sorted(containers, key = lambda x: int(x[0]),  reverse=True)

block = [containers[0]]
for container in containers.copy():
    if int(block[-1][0]) - int(container[0]) >= 7:
        if block[-1][1] != container[1]:
            block += [container]