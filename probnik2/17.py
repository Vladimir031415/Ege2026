A = []
for i in range(10000):
    A.append(int(input()))
B = []
for i in A:
    if abs(i) % 41 == 0:
        B.append(i)
z = min(B)
ch = 0
C = []
for i in range(len(A)-1):
    if abs(A[i]-A[i+1]) % z == 0 and (A[i]-A[i+1]) != 0:
        ch += 1
        C.append(A[i]+A[i+1])
print(ch)
print(max(C))

