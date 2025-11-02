print("x y w z |   f")
for x in (1, 0):
    for y in (1, 0):
        for w in (1, 0):
            for z in (1, 0):
                f = (z<=y) or ((w<=x)<=y)
                if f==0: print(x, y, w, z, '|', f)
