from turtle import *
k = 7
tracer(0)
up()
for x in range(-70, 70):
    for y in range(-70, 70):
        goto(x*k, y*k)
        dot(3)
goto(0, 0)
dot(5, "red")
left(90)
down()

fd(30*k)
left(60)
fd(24*k)
right(240)
fd(54*k)
left(120)
fd(24*k)
left(60)

up()
fd(30*k)
right(90)
fd(20*k)
left(90)
down()

for i in range(17):
    down()
    fd(6*k)
    left(90)
    fd(80*k)
    left(90)
