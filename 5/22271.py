a = []
for n in range(200):
    N = oct(n)[2:]
    if N[0] == 5:
        N.replace("2", "*")
        N.replace("1", "2")
        N.replace("*", "1")
        N = "11" + N
    else:
        N = "2" + N[1:] + "10"
    if int(N, 8) < 1354:
        a.append(n)
print(max(a))
