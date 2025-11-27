def c(a):
    r = ""
    while a:
        r+= str(a%7)
        a//=7
    return r[::-1]
a = []
for i in range(2030):
    x = 2030-i
    if c(7**170 + 7**100 - x).count("0") == 73:
        print(x)
