
def c(a):
    r = ""
    while a:
        r+= str(a%11)
        a//=11
    return r[::-1]

for i in range(3000):
    x = 3000-i
    if c(9*11**210 + 8*11**150 - x).count("0") == 60:
        print(x)
        break