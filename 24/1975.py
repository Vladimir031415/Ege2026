data = input()

data = data.replace("PP","P P").replace("PP","P P")
data = data.split()
print(max(map(len, data)))