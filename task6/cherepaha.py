from turtle import *
tracer(4)
screensize(10000,10000)

m = 20
k = 1
#up()
# bk(2.7*m)
# rt(90)
# bk(m*0.7)
# lt(90)
# down()
for g in range(100):
    for i in range(362):
        fd(m*k)
        rt(i)
    k = k*0.99
    rt(45)



up()
# for x in range(-50,50):
#     for y in range(-50,50):
#         goto(x*m,y*m)
#         dot(3, "red")
#
# print(29*19+31*8-8*15)
done()