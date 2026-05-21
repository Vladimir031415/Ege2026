#from re import finditer
#data = input()
#pattern = "[^P]*(P[^P]+)*P?"
#
#matches = [match.group() for match in finditer(pattern, data)]
#print(len(max(matches, key=len)))

data = input()
res = []
cnt = 0
for i in range(len(data)):
    if not(data[i] == "P" and data[i+1] == "P"):
        cnt += 1
    else:7
        res.append(cnt)
        cnt = 0
res.append(cnt)

print(max(res))