a = []

for A in range(300):
    for x in range(100):
        for y in range(100):
            if (9*x + y > A) or (x >= 36) or (y >= 18):
                a.append(A)
print(max(a))

