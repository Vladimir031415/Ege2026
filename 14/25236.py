for p in range(11,37):
    S1 = int("29a1", p) + int("47771", p) + int("12a", p)
    for x in range(1, 500001):
        if S1 == 1000000 + x:
            print(p)
            break