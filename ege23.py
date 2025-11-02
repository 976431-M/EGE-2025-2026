from math import *
def f(x, y):
    if x<y or x == 20:
        return 0
    if x == y:
        return 1
    return f(x-2, y) + f(x-3, y) + f(int(sqrt(x)), y)

print(f(26, 3))
