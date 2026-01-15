a = 3*17**777 + 15*17**250 - 6*17**100 + 2
b = []
while a:
    if a%17%2 == 0:
        b.append(a%17)
    a //= 17
print(len(set(b)))