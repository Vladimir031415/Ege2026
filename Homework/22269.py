def c(a):
    r = ""
    while a:
        r+= str(a%5)
        a//=5
    return r[::-1]


for i in range(10,200):
    N = c(i)
    if N[-1]=="0":
        N.replace("1","a")
        N.replace("4", "1")
        N.replace("a", "4")
        N = "33" + N
    else:
        N = "3" + N[1:] + "42"
    R = int(N, 5)
    if R <= 1992:
        print(i,R)

