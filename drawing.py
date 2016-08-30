import turtle
import math
bob = turtle.Turtle()

"""definitions for circle"""
def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def circle(t, r):
    arc(t, r, 360)

"""sun"""
bob.pencolor("yellow")
bob.pensize(5)
bob.pu()
bob.backward(+150)
bob.lt(90)
bob.backward(-170)
bob.pd()

circle(bob, 75)

"""position for roof"""
bob.pu()
bob.backward(+180)
bob.rt(90)
bob.forward(+175)
bob.pd()

"""roof"""
bob.pencolor("black")
bob.fd(230)
bob.lt(120)
bob.fd(230)
bob.lt(120)
bob.fd(230)

"""position for house"""
bob.pu()
bob.lt(120)
bob.fd(15)
bob.pd()

"""house"""
bob.pencolor("black")
bob.rt(90)
bob.fd(200)
bob.lt(90)
bob.fd(75)
bob.lt(90)

"""door"""
bob.pencolor("blue")
bob.fd(75)
bob.rt(90)
bob.fd(50)
bob.rt(90)
bob.fd(75)
bob.rt(90)
bob.fd(50)
bob.lt(90)
bob.lt(90)
bob.fd(50)

"""remainder of house"""
bob.pencolor("black")
bob.fd(75)
bob.lt(90)
bob.fd(200)

"""position for window"""
bob.pencolor("blue")
bob.pu()
bob.lt(90)
bob.backward(-180)
bob.rt(90)
bob.backward(+95)
bob.pd()

"""window"""
bob.fd(50)
bob.rt(90)
bob.fd(50)
bob.rt(90)
bob.fd(50)
bob.rt(90)
bob.fd(50)

"""position for second window"""
bob.pu()
bob.lt(90)
bob.lt(90)
bob.forward(+100)
bob.pd()

"""second window"""
bob.lt(90)
bob.fd(50)
bob.rt(90)
bob.fd(50)
bob.rt(90)
bob.fd(50)
bob.rt(90)
bob.fd(50)

"""position for grass"""
bob.pensize(20)
bob.pu()
bob.lt(90)
bob.forward(+105)
bob.lt(90)
bob.forward(-440)
bob.pd()

"""grass"""
bob.pencolor("green")
bob.forward(+300)

bob.hideturtle()

turtle.mainloop()
turtle.done()

