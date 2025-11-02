from itertools import *
a = permutations('0123456789abcdefg', 6)
cou = 0
for x in a:
    num = ''.join(x)
    if num[0] != '0':
        for l in num:
            if l in '02468aceg':
                num = num.replace(l, 'q')
            else:
                num = num.replace(l, 'w')
        if 'qqq' not in num and 'www' not in num:
            cou += 1
print(cou)
