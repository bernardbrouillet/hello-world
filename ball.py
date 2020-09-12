import turtle
import math

def forces(x,y):
    r2 = x*x + y*y
    r = math.sqrt(r2)
    f = 100000.0/r2
    fx = -f * x/r
    fy = -f * y/r
    return (fx, fy)

earth = turtle.Turtle()
earth.shape("circle")
earth.penup()
earth.color("blue")

moon = turtle.Turtle()
moon.shape("circle")
moon.penup()
moon.color("orange")

x =    0.0
y = -200.0
vx = 25.0
vy = 0.0
dt = 0.1

for i in range(2000):
    (fx, fy) = forces(x,y)
    vx = vx + fx*dt
    vy = vy + fy*dt
    x = x + vx*dt
    y = y + vy*dt
    moon.setpos(x,y)

turtle.done()
