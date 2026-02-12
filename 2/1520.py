from itertools import *
def f(a, b, c):
    return (a<=b) and ((a and b) <= (not c))
table = [
    (0, 0, 0, 1),
    (0,0, 1, 0),
    (0, 1, 0, 1)
    (0, 1, 1, 1)

]
