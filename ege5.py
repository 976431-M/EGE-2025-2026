def f(n):
    bn = bin(n)[2::]
    if n%2 == 0:
        new = bn.replace('0', '1', bn.count('0'))
    else:
        if bn[0] != '1':
            new = bn.replace('1', '00', bn.count('1'))
        else:
            new0 = bn.replace('1', '00', bn.count('1'))
            new = '1' + new0[2::]
    return int(str(new), 2)
        
for n in range(2000):
    if f(n) <= 600:
        print(n, f(n))
