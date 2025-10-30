# module Turtle
from turtle import *

# движение черепахи вперёд по направлению головы.
forward(100)
fd(20)

# движение черепахи назад.
backward(30)
bk(20)

# right
right(90)
rt(90)

# left
left(90)
lt(90)

#podnyati
up()

#opustit
down()

#otkluchenie

tracer(0)
update()

#размер холста
screensize(3000,3000)

#tchk
up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*m,y*m)
        dot(3, "red")



done()
