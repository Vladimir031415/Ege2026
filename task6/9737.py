
from turtle import *
screensize(3000,3000)
tracer(0)
m = 30

for i in range(1,3):

    fd(10*m)
    rt(90)
    fd(18*m)
    rt(90)

up()

fd(5*m)
rt(90)
fd(7*m)
lt(90)

down()

for i in range(1,3):
    fd(10*m)
    rt(90)
    fd(7*m)
    rt(90)

up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*m,y*m)
        dot(3, "red")



print(249)
update()
done()



