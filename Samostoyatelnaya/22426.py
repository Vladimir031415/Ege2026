a = 15*343**2031 + 7*49**1142 - 3*7**111 + 7*222 - 16809
ch = 0
nch = 0
while a:
    if (a % 7)%2 == 0:
        ch+=1
    else:
        nch+=1
    a//=7
print(ch-nch)

