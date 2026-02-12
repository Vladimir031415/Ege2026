a = []
for A in range(1, 200):
    if all((x%A == 0 or x%23 == 0) <= ( x not in range(50,71)) for x in range(1,200)):
        a.append(A)
print(a)
