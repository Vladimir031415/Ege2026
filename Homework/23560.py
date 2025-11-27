
def c(a):
    r = ""
    while a:
        r+= str(a%9)
        a//=9
    return r[::-1]

for i in range(2400):
    x = 2400-i
    if c(7*9**210 + 6*9**110 - x).count("0") == 100:
        print(x)
        break