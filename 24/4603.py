data = input()
res = []
r = 0
poslednya = ""
glasni = ("A", "O", "")
soglasni = ("B", "C", "D", "")
for i in data:
    if poslednya in glasni:
        if i in soglasni:
            r += 1
            poslednya = i
        else:
            res.append(r)
            r = 1
            poslednya = i
    if poslednya in soglasni:
        if i in glasni:
            r += 1
            poslednya = i
        else:
            res.append(r)
            r = 1
            poslednya = i

from re import finditer
data = input()
a = data.replace("O", "A").replace("C", "B").replace("D", "B")
pattern = "([BCD][AO])+"
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len))//2)