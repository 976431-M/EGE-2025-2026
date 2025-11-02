a = 3*(17**777) + 15*(17**250) - 6*(17**100) + 2
def f(n):
    num = ''
    digits = '0123456789ABCDEFG'
    while n > 0:
        num += digits[n%17]
        n = n//17
    num = num[::-1]
    return num
na = f(a)
mas = set()
for x in na:
    if x in '02468ACEG':
        mas.add(x)

print(mas)
