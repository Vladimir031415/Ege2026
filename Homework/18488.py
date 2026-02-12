def s(a):
    r = ""
    while a:
        r += str(a%7)
        a //= 7
    return r[::-1]




for x in range(1000):
    if s(7**666 + 7**333 + 49**x - 343).count("6") == 49:
        print(x)
        break


