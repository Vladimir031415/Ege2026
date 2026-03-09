data = input()

data = data.split('Y')
c = []
for i in range(len(data)-80):
    minidata = "Y".join(data[i:i+81])
    if minidata.count('2025')>=90:
        c.append(len(minidata))

print(max(c))
