def dig(x, y):
    if str(x)[0] == str(y)[0]:
        return 1
    else:
        return 0

def f(x, a):
    return ((1-dig(x, 28)) and dig(x, 47)) <= (x>(a-20))

for a in range(1, 100):
    if all(f(x, a) for x in range(1, 100)) == 1:
        print(a)
