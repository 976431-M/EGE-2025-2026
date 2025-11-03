def dels(n):
    res = []
    for d in range(2, n//2+1):
        if n%d == 0 and all((d%x) != 0 for x in range(2, d)):
            res.append(d)
            n = n//d
    return set(res)

def sred(x):
    mas = []
    for num in x:
        if num%10 == 7:
            mas.append(num)
    if len(mas) != 0:
        return sum(mas)//len(mas)
    else:
        return 0

k = 0   
for x in range(750000, 740000, -1):
    F = sred(dels(x))
    if k == 5:
        break
    if F != 0 and F%111 == 0:
        print(x, F)
        k += 1
    
